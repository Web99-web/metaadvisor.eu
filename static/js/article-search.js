(function () {
  'use strict';
  const normalize = value => String(value || '').replace(/https?:\/\/[^\s<>]+/giu, ' ').replace(/\b(?:www\.)?metaadvisor\.eu\b/giu, ' ').normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase();
  const tokens = value => normalize(value).match(/[\p{L}\p{N}]+/gu) || [];
  const lexicon = [
    ['btc', 'bitcoin'], ['eth', 'ethereum', 'ether'], ['sol', 'solana'],
    ['ai', 'ki', 'artificial intelligence', 'umjetna inteligencija', 'kunstliche intelligenz'],
    ['moderation', 'moderacija', 'moderacije', 'moderaciju', 'moderacijom', 'moderiranje', 'moderiranja'],
    ['disabled', 'blocked', 'banned', 'suspended', 'deactivated', 'blokirani', 'blokiranih', 'blokirane', 'blokiran', 'ugaseni', 'ugasene', 'gesperrt', 'gesperrte', 'gesperrten', 'deaktiviert', 'deaktivierte', 'deaktivierten'],
    ['account', 'accounts', 'profile', 'profiles', 'racun', 'racuna', 'racuni', 'racune', 'profil', 'profila', 'profili', 'profile', 'konto', 'konten', 'kontos']
  ];
  const phrase = value => tokens(value).join(' ');
  const fields = ['title', 'summary', 'tags', 'headings', 'content'];
  function prepare(rows) {
    return rows.map((row, order) => {
      const text = fields.map(k => phrase(Array.isArray(row[k]) ? row[k].join(' ') : row[k]));
      return { row, order, text, sets: text.map(s => new Set(s.split(' '))) };
    });
  }
  function contains(doc, index, term) {
    return term.includes(' ') ? (' ' + doc.text[index] + ' ').includes(' ' + term + ' ') : doc.sets[index].has(term);
  }
  function metaFocus(doc) {
    const brand = /(?:^| )(?:meta|mete|metin|metina|metini|metas)(?: |$)/;
    const product = /(?:^| )(?:facebook|facebooku|facebooks|instagram|instagramu|instagrams|whatsapp|whatsappa|threads)(?: |$)/;
    // A passing mention deep in the body is insufficient for the company entity.
    if (brand.test(doc.text[0]) && /(?:^| )(?:metaplanet|metamask)(?: |$)/.test(doc.text[0])) return false;
    if (/(?:^| )(?:kriva meta|wrong target|falsches ziel)(?: |$)/.test(doc.text[0])) return false;
    const mentions = doc.text[4].split(' ').filter(t => /^(?:meta|mete|metin|metas|facebook(?:a|u|om|s)?|instagram(?:a|u|om|s)?|whatsapp(?:a|u|om|s)?)$/.test(t)).length;
    const multipleProducts = /(?:^| )facebook(?:a|u|om|s)?(?: |$)/.test(doc.text[4]) && /(?:^| )instagram(?:a|u|om|s)?(?: |$)/.test(doc.text[4]);
    const corporate = /(?:^| )(?:zuckerberg|llama|meta platforms|meta ai|oversight board)(?: |$)/.test(doc.text.join(' '));
    if (brand.test(doc.text[0]) && (product.test(doc.text.join(' ')) || corporate)) return true;
    if (product.test(doc.text[0]) && (brand.test(doc.text[4]) || doc.sets[2].has('meta') || mentions >= 4)) return true;
    if (brand.test(doc.text[1]) && product.test(doc.text.slice(0, 4).join(' '))) return true;
    if (product.test(doc.text[1]) && (brand.test(doc.text[4]) || /(?:^| )(?:moderation|moderacija|gesperrt|banned|disabled)(?: |$)/.test(doc.text[1]))) return true;
    if ((brand.test(doc.text[4]) || multipleProducts) && product.test(doc.text[4]) && mentions >= 4 && /(?:^| )(?:moderation|moderacija|moderacije|appeals|zalbe|beschwerden)(?: |$)/.test(doc.text[3])) return true;
    return doc.sets[2].has('meta') && product.test(doc.text[3]);
  }
  function search(docs, query) {
    const queryTokens = tokens(query);
    if (!queryTokens.length) return [];
    // Consume known multiword aliases as a single concept, keeping AND between concepts.
    const groups = [];
    for (let i = 0; i < queryTokens.length; i++) {
      const pair = queryTokens.slice(i, i + 2).join(' ');
      let aliases = lexicon.find(g => g.includes(pair));
      if (aliases) i++;
      else aliases = lexicon.find(g => g.includes(queryTokens[i])) || [queryTokens[i]];
      groups.push(aliases);
    }
    const meta = queryTokens.includes('meta');
    const weights = [12, 7, 5, 4, 1];
    const result = [];
    docs.forEach(doc => {
      if (meta && !metaFocus(doc)) return;
      let score = 0;
      for (const aliases of groups) {
        if (meta && aliases.length === 1 && aliases[0] === 'meta') {
          const entityTerms = ['meta', 'mete', 'metin', 'metina', 'metini', 'metas', 'facebook', 'facebooku', 'facebooks', 'instagram', 'instagramu', 'whatsapp', 'threads'];
          fields.forEach((_, i) => { if (entityTerms.some(term => contains(doc, i, term))) score += weights[i]; });
          continue;
        }
        let best = 0;
        fields.forEach((_, i) => { if (aliases.some(term => contains(doc, i, term))) best = Math.max(best, weights[i]); });
        if (!best) return;
        score += best;
      }
      const exact = queryTokens.join(' ');
      if (queryTokens.length > 1) doc.text.forEach((s, i) => { if ((' ' + s + ' ').includes(' ' + exact + ' ')) score += weights[i]; });
      result.push({ row: doc.row, score, order: doc.order });
    });
    return result.sort((a, b) => b.score - a.score || String(b.row.date).localeCompare(String(a.row.date)) || a.order - b.order);
  }
  const engine = { normalize, tokens, prepare, search };
  if (typeof module !== 'undefined' && module.exports) { module.exports = engine; return; }
  if (typeof document === 'undefined') {
    let data;
    self.onmessage = async event => {
      const m = event.data;
      try {
        if (!data) data = fetch(m.path, { credentials: 'omit' }).then(r => { if (!r.ok) throw Error('Index HTTP ' + r.status); return r.json(); }).then(prepare).catch(e => { data = null; throw e; });
        const ranked = search(await data, m.query);
        const page = Math.max(0, Math.min(m.page || 0, Math.max(0, Math.ceil(ranked.length / 30) - 1)));
        self.postMessage({ id: m.id, total: ranked.length, page, rows: ranked.slice(page * 30, (page + 1) * 30).map(x => {
          const { title, url, date, summary, image } = x.row; return { title, url, date, summary, image };
        }) });
      } catch (e) { self.postMessage({ id: m.id, error: true }); }
    };
    return;
  }
  const form = document.getElementById('onsite-search-form');
  if (!form) return;
  const input = document.getElementById('q'), grid = document.getElementById('search-results');
  const count = document.getElementById('search-count'), pager = document.getElementById('search-pages');
  const lang = (document.documentElement.lang || 'en').split('-')[0];
  const words = lang === 'hr' ? ['Pronađeno članaka: ', 'Prethodna', 'Sljedeća', 'Učitavanje…', 'Pretraga nije dostupna. Pokušajte ponovno.'] : lang === 'de' ? ['Gefundene Artikel: ', 'Zurück', 'Weiter', 'Laden…', 'Suche nicht verfügbar. Bitte erneut versuchen.'] : ['Articles found: ', 'Previous', 'Next', 'Loading…', 'Search unavailable. Please try again.'];
  const path = (lang === 'hr' || lang === 'de' ? '/' + lang : '') + '/index.json';
  let worker, serial = 0, page = 0, timer;
  const escape = s => String(s || '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const localURL = value => { try { const u = new URL(value, location.origin); return u.origin === location.origin && !u.username && !u.password ? u.pathname + u.search + u.hash : '#'; } catch (_) { return '#'; } };
  function render(m) {
    if (m.id !== serial) return;
    if (m.error) { count.textContent = words[4]; grid.replaceChildren(); pager.replaceChildren(); return; }
    page = m.page; count.textContent = words[0] + m.total;
    grid.innerHTML = m.rows.map(it => {
      const url = escape(localURL(it.url)), img = escape(localURL(it.image || '/images/placeholder-metaadvisor-small.jpg'));
      const date = /^\d{4}-\d{2}-\d{2}$/.test(it.date) ? it.date.slice(8) + '.' + it.date.slice(5, 7) + '.' + it.date.slice(0, 4) + '.' : '';
      return '<div class="card"><a href="' + url + '" target="_blank" rel="noopener"><img loading="lazy" class="card-img" src="' + img + '" alt="' + escape(it.title) + '"></a><div class="card-body"><div class="card-meta">' + date + '</div><h3 class="card-title"><a href="' + url + '" target="_blank" rel="noopener">' + escape(it.title) + '</a></h3><p class="card-summary">' + escape(it.summary) + '</p></div></div>';
    }).join('');
    pager.replaceChildren();
    if (m.total > 30) {
      [[words[1], page - 1, page === 0], [words[2], page + 1, (page + 1) * 30 >= m.total]].forEach(([label, next, disabled]) => {
        const button = document.createElement('button'); button.type = 'button'; button.textContent = label; button.disabled = disabled; button.addEventListener('click', () => request(next)); pager.append(button);
      });
      const position = document.createElement('span'); position.textContent = ' ' + (page + 1) + ' / ' + Math.ceil(m.total / 30); pager.append(position);
    }
  }
  function request(next) {
    serial++;
    if (!input.value.trim()) { count.textContent = ''; grid.replaceChildren(); pager.replaceChildren(); return; }
    count.textContent = words[3];
    try {
      if (!worker) { worker = new Worker('/js/article-search.js'); worker.onmessage = e => render(e.data); worker.onerror = () => { count.textContent = words[4]; worker.terminate(); worker = null; }; }
      worker.postMessage({ id: serial, query: input.value, page: next, path });
    } catch (_) { count.textContent = words[4]; }
  }
  form.addEventListener('submit', e => { e.preventDefault(); clearTimeout(timer); request(0); });
  input.addEventListener('input', () => { serial++; clearTimeout(timer); timer = setTimeout(() => request(0), 180); });
})();
