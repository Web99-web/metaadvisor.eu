/* MetaAdvisor: consent-first, single GA4 owner. No production test switch. */
(function (w, d) {
  'use strict';
  if (w.MAConsent) return;
  var cfg = w.MA_GA_CONFIG || {}, id = cfg.measurementId || 'G-KL111KNH3S';
  var key = 'ma_consent_v2', maxAge = 180 * 24 * 60 * 60 * 1000;
  var visitKey = 'ma_analytics_visit_v1', preferenceCookie = 'ma_analytics_choice', visitCookie = 'ma_analytics_visit';
  var visitIdle = 30 * 60 * 1000, choiceRecord = null, choiceRevision = 0, geoPromise = null;
  var loaded = false, sent = false, choice = null, mode = 'pending', country = 'UNKNOWN', region = '', geoSource = 'unknown';
  var regionalDecision = {regime:'unresolved', rule:'location-pending', ga4:'off', banner:false};
  w.dataLayer = w.dataLayer || [];
  w.gtag = w.gtag || function () { w.dataLayer.push(arguments); };
  var disabled = 'ga-disable-' + id;
  w[disabled] = true;
  function parameters(analytics) {
    return {analytics_storage: analytics ? 'granted' : 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied'};
  }
  w.gtag('consent', 'default', parameters(false));
  w.gtag('set', 'ads_data_redaction', true);
  w.gtag('set', 'url_passthrough', false);
  function privacySignal() { return w.navigator.globalPrivacyControl === true || w.navigator.doNotTrack === '1'; }
  function sixMonthsAfter(at) {
    var date = new Date(at), day = date.getUTCDate();
    date.setUTCDate(1); date.setUTCMonth(date.getUTCMonth() + 6);
    var end = new Date(date); end.setUTCMonth(end.getUTCMonth() + 1, 0);
    date.setUTCDate(Math.min(day, end.getUTCDate())); return date.getTime();
  }
  function fromJSON(raw) { try { return raw ? JSON.parse(raw) : null; } catch (_) { return null; } }
  function getCookie(name) {
    var raw; try { raw = d.cookie || ''; } catch (_) { return null; }
    var prefix = name + '=', parts = raw.split(';');
    for (var i = 0; i < parts.length; i++) {
      var part = parts[i].trim(); if (part.indexOf(prefix) === 0) { try { return decodeURIComponent(part.slice(prefix.length)); } catch (_) { return null; } }
    }
    return null;
  }
  function setCookie(name, value, seconds) {
    try {
      var secure = new URL(w.location.href).protocol === 'https:' ? '; Secure' : '';
      d.cookie = name + '=' + encodeURIComponent(value) + '; Path=/; SameSite=Lax' + secure + (typeof seconds === 'number' ? '; Max-Age=' + seconds : '');
      return seconds === 0 ? getCookie(name) === null : getCookie(name) === value;
    } catch (_) { return false; }
  }
  function storageArea(name) { try { return w[name]; } catch (_) { return null; } }
  function storageRead(storage, name) { try { return storage.getItem(name); } catch (_) { return null; } }
  function storageWrite(storage, name, value) { try { storage.setItem(name, value); return storage.getItem(name) === value; } catch (_) { return false; } }
  function storageRemove(storage, name) { try { storage.removeItem(name); } catch (_) {} }
  function clearPersistent() { storageRemove(storageArea('localStorage'), key); storageRemove(storageArea('localStorage'), 'ma_consent'); setCookie(preferenceCookie, '', 0); }
  function clearVisit() { storageRemove(storageArea('sessionStorage'), visitKey); storageRemove(storageArea('localStorage'), visitKey + '_fallback'); setCookie(visitCookie, '', 0); }
  function valid(record) {
    if (!record || record.version !== cfg.policyVersion || !/^(granted|denied)$/.test(record.analytics) || typeof record.at !== 'number' || record.at > Date.now()) return false;
    if (record.scope === 'visit') return record.analytics === 'denied' && typeof record.lastSeen === 'number' && record.lastSeen <= Date.now() && Date.now() - record.lastSeen < visitIdle;
    var expires = typeof record.expiresAt === 'number' ? Math.min(record.expiresAt, sixMonthsAfter(record.at)) : record.at + maxAge;
    return Date.now() < expires;
  }
  function saveVisit(record) {
    record = Object.assign({}, record, {scope:'visit', lastSeen:Date.now()}); delete record.expiresAt;
    var raw = JSON.stringify(record), storedTab = storageWrite(storageArea('sessionStorage'), visitKey, raw), storedCookie = setCookie(visitCookie, raw);
    var storedFallback = false;
    if (!storedCookie) storedFallback = storageWrite(storageArea('localStorage'), visitKey + '_fallback', raw);
    else storageRemove(storageArea('localStorage'), visitKey + '_fallback');
    return storedTab || storedCookie || storedFallback;
  }
  function savePersistent(record) {
    var raw = JSON.stringify(record), storedLocal = storageWrite(storageArea('localStorage'), key, raw);
    return setCookie(preferenceCookie, raw, Math.max(0, Math.floor((record.expiresAt - Date.now()) / 1000))) || storedLocal;
  }
  function stored() {
    var candidates = [fromJSON(storageRead(storageArea('localStorage'), key)), fromJSON(getCookie(preferenceCookie)), fromJSON(storageRead(storageArea('sessionStorage'), visitKey)), fromJSON(getCookie(visitCookie)), fromJSON(storageRead(storageArea('localStorage'), visitKey + '_fallback'))].filter(valid);
    candidates.sort(function (a,b) {
      if (a.at !== b.at) return b.at - a.at;
      if (a.analytics !== b.analytics) return a.analytics === 'denied' ? -1 : 1;
      if ((a.scope === 'visit') !== (b.scope === 'visit')) return a.scope === 'visit' ? 1 : -1;
      return 0;
    });
    if (candidates.length) {
      choiceRecord = candidates[0]; if (choiceRecord.scope === 'visit') { choiceRecord=Object.assign({},choiceRecord,{lastSeen:Date.now()}); saveVisit(choiceRecord); }
      return choiceRecord.analytics;
    }
    clearVisit();
    // Previously stored explicit refusals are not silently shortened by this update.
    if (storageRead(storageArea('localStorage'), 'ma_consent') === 'denied') {
      // Give legacy refusals a bounded validity; never turn them into consent.
      choiceRecord = {version:cfg.policyVersion, schema:2, analytics:'denied', at:Date.now(), scope:'legacy-refusal'};
      choiceRecord.expiresAt=sixMonthsAfter(choiceRecord.at);
      savePersistent(choiceRecord); storageRemove(storageArea('localStorage'), 'ma_consent');
      return 'denied';
    }
    choiceRecord = null; return null;
  }
  function notify(record) {
    // This is a cross-tab notification, never an authority for a later visit.
    try { storageArea('localStorage').setItem(key + '_signal', JSON.stringify(record)); storageArea('localStorage').removeItem(key + '_signal'); } catch (_) {}
  }
  function retainRefusal(countryCode) { return (cfg.refusalRetentionCountries || ['FR','GB']).indexOf(countryCode) !== -1 || countryCode === 'UNKNOWN'; }
  function showRefusalBanner() {
    // Reoffer the choice on a new page load in banner regions; never override refusal.
    return choice === 'denied' && !privacySignal();
  }
  function locationReady() {
    if (!geoPromise) geoPromise = locate().then(function (geo) { country=geo.country; region=geo.region; geoSource=geo.source; return geo; });
    return geoPromise;
  }
  function settleRefusal(record, revision) {
    if (choiceRevision !== revision || choice !== 'denied') return;
    var newer=[fromJSON(storageRead(storageArea('localStorage'),key)),fromJSON(getCookie(preferenceCookie)),fromJSON(getCookie(visitCookie))].some(function (x) { return valid(x) && x.at > record.at; });
    if (newer) return;
    if (retainRefusal(country)) {
      record = Object.assign({}, record, {scope:country === 'UNKNOWN' ? 'unresolved-region' : 'regional-refusal', expiresAt:sixMonthsAfter(record.at)});
      choiceRecord = record; savePersistent(record);
    } else {
      clearPersistent(); record = Object.assign({}, record, {scope:'visit', lastSeen:Date.now()}); delete record.expiresAt;
      choiceRecord=record; saveVisit(record);
    }
    notify(record);
  }
  function remember(value, revision) {
    var record = {version:cfg.policyVersion, schema:2, analytics:value, at:Date.now()};
    clearPersistent(); clearVisit();
    if (value === 'granted') {
      record.scope='persistent'; record.expiresAt=sixMonthsAfter(record.at); choiceRecord=record; savePersistent(record); notify(record); return;
    }
    record.scope='visit'; record.lastSeen=record.at; choiceRecord=record; saveVisit(record);
    if (country === 'UNKNOWN') {
      record.scope='pending-region'; record.expiresAt=sixMonthsAfter(record.at); choiceRecord=record; savePersistent(record); notify(record);
      locationReady().then(function () { settleRefusal(record,revision); });
    } else settleRefusal(record,revision);
  }
  function canRememberVisit() {
    var probe = visitKey + '_probe';
    if (storageWrite(storageArea('sessionStorage'), probe, '1')) { storageRemove(storageArea('sessionStorage'), probe); return true; }
    var ok = setCookie(probe,'1'); setCookie(probe,'',0);
    if (ok) return true;
    ok = storageWrite(storageArea('localStorage'), probe, '1'); storageRemove(storageArea('localStorage'), probe); return ok;
  }
  function clearAnalyticsCookies() {
    var raw; try { raw = d.cookie || ''; } catch (_) { return; }
    raw.split(';').forEach(function (entry) {
      var name = entry.split('=')[0].trim();
      if (!/^(_ga(?:_|$)|_gid$|_gat(?:_|$))/.test(name)) return;
      [null, w.location.hostname, '.metaadvisor.eu'].forEach(function (domain) {
        try { d.cookie = name + '=; Max-Age=0; path=/; SameSite=Lax' + (domain ? '; domain=' + domain : ''); } catch (_) {}
      });
    });
  }
  function cleanURL(value) {
    if (!value) return '';
    try { var u = new URL(value, w.location.href); return u.origin + u.pathname; } catch (_) { return ''; }
  }
  function resolveRegionalPolicy(geo) {
    var policy = cfg.regionalPolicy || {}, regimes = policy.regimes || {}, groups = policy.jurisdiction_groups || {};
    var globalDraft = policy.global_measurement_proposal || {};
    var draftMeasurement = globalDraft.enabled === true && globalDraft.transport === 'cookieless';
    var unresolved = {regime:'unresolved', rule:draftMeasurement ? 'global-cookieless-local-proposal' : 'no-applicable-basis', ga4:draftMeasurement ? 'cookieless' : 'off', banner:!draftMeasurement};
    if (policy.schema !== 1 || !geo || !/^[A-Z]{2}$/.test(geo.country) || geo.country === 'XX') return unresolved;
    var matches = (policy.rules || []).filter(function (rule) {
      return (rule.groups || []).some(function (name) {
        var group = groups[name]; if (!group) return false;
        if (group.trusted_region_required && geo.source !== 'edge-metadata') return false;
        return (group.countries || []).indexOf(geo.country) !== -1 ||
          (!!geo.region && (group.regions || []).indexOf(geo.country + '-' + geo.region) !== -1);
      });
    });
    // A consent rule wins if later evidence creates an overlapping classification.
    var selected = matches.find(function (r) { return r.regime === 'prior_consent'; }) ||
      matches.find(function (r) { return r.regime === 'automatic' && !!r.basis && /^(cookies|cookieless)$/.test(r.ga4); });
    if (!selected || !regimes[selected.regime]) return unresolved;
    return {regime:selected.regime, rule:selected.id, ga4:selected.ga4, banner:regimes[selected.regime].banner === true};
  }
  function cookielessAllowed(why) {
    return why === 'regional-policy' && !choice && !privacySignal() &&
      (regionalDecision.regime === 'automatic' || regionalDecision.regime === 'unresolved') && regionalDecision.ga4 === 'cookieless';
  }
  function startGA() {
    if (loaded) return;
    loaded = true;
    w.gtag('js', new Date());
    w.gtag('config', id, {send_page_view: false, allow_google_signals: false, allow_ad_personalization_signals: false, cookie_expires: 60 * 60 * 24 * 180, page_location: cleanURL(w.location.href), page_referrer: cleanURL(d.referrer || '')});
    var s = d.createElement('script'); s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    d.head.appendChild(s);
  }
  function apply(allowed, why) {
    allowed = allowed && !privacySignal();
    var cookieless = !allowed && cookielessAllowed(why);
    mode = cookieless ? 'cookieless-denied-storage' : (allowed ? why : (privacySignal() ? 'privacy-signal' : why));
    w[disabled] = !(allowed || cookieless);
    var toggle = d.getElementById('ma-analytics-toggle'), status = d.getElementById('ma-cookie-status');
    if (toggle) { toggle.checked = !!allowed; toggle.disabled = privacySignal(); }
    if (status) status.textContent = privacySignal() ? 'Analytics is off because your browser requests privacy protection.' : (cookieless ? 'Basic measurement without analytics cookies is on. Save settings with the optional box unchecked to stop measurement.' : (allowed ? 'Analytics is on. Uncheck the optional box and save to turn it off.' : 'Analytics is off. Check the optional box and save to turn it on.'));
    w.gtag('consent', 'update', parameters(allowed));
    if (!allowed) { clearAnalyticsCookies(); if (!cookieless) return; }
    startGA();
    if (!sent) {
      sent = true;
      w.gtag('event', 'page_view', {page_location: cleanURL(w.location.href), page_referrer: cleanURL(d.referrer || ''), page_title: d.title});
    }
  }
  function banner(show) { var e = d.getElementById('ma-consent'); if (e) e.hidden = !show; }
  function choose(value) {
    choice = value; choiceRevision++;
    apply(value === 'granted', value === 'granted' ? 'explicit-consent' : 'explicit-refusal'); banner(false);
    remember(value, choiceRevision);
  }
  async function locate() {
    var embedded = w.MA_EDGE_REGION;
    if (embedded && embedded.schema === 1 && /^[A-Z]{2}$/.test(embedded.country) && embedded.country !== 'XX') {
      return {country:embedded.country, region:/^[A-Z0-9]{1,3}$/.test(embedded.region || '') ? embedded.region : '', source:'edge-metadata'};
    }
    var timeoutMs = Math.min(60000, Math.max(1000, Number(cfg.locationTimeoutMs) || 60000));
    var controller = new AbortController(), timeout = w.setTimeout(function () { controller.abort(); }, timeoutMs);
    try {
      try {
        var edge = await w.fetch('/_ma/region', {cache: 'no-store', credentials: 'omit', signal: controller.signal});
        if (edge.ok) {
          var g = await edge.json();
          if (g && g.schema === 1 && /^[A-Z]{2}$/.test(g.country) && g.country !== 'XX') {
            return {country:g.country, region:/^[A-Z0-9]{1,3}$/.test(g.region || '') ? g.region : '', source:'edge-metadata'};
          }
        }
      } catch (_) { /* An unavailable endpoint never grants regional permission. */ }
      var r = await w.fetch('/cdn-cgi/trace', {cache: 'no-store', credentials: 'omit', signal: controller.signal});
      if (!r.ok) return {country:'UNKNOWN',region:'',source:'unknown'};
      var m = (await r.text()).match(/^loc=([A-Z]{2})\s*$/m);
      return {country:m && m[1] !== 'XX' ? m[1] : 'UNKNOWN',region:'',source:'trace-country-only'};
    } catch (_) { return {country:'UNKNOWN',region:'',source:'unknown'}; }
    finally { w.clearTimeout(timeout); }
  }
  async function boot() {
    var accept = d.getElementById('ma-accept'), reject = d.getElementById('ma-decline'), settings = d.getElementById('ma-consent-settings');
    if (accept) accept.addEventListener('click', function () { choose('granted'); });
    if (reject) reject.addEventListener('click', function () { choose('denied'); });
    if (settings) settings.addEventListener('click', function () { banner(true); });
    var close = d.getElementById('ma-consent-close');
    if (close) close.addEventListener('click', function () { choose('denied'); });
    var cookieForm = d.getElementById('ma-cookie-form');
    if (cookieForm) cookieForm.addEventListener('submit', function (event) {
      event.preventDefault();
      var toggle = d.getElementById('ma-analytics-toggle');
      choose(toggle && toggle.checked ? 'granted' : 'denied');
    });
    if (privacySignal()) { apply(false,'privacy-signal'); banner(false); return; }
    choice = stored();
    if (choice === 'granted') { apply(true,'stored-granted'); banner(false); return; }
    var bootRevision = choiceRevision;
    // Page rendering and footer controls do not wait on this asynchronous lookup.
    // Unresolved geography offers a choice; it never grants Google permission.
    await locationReady();
    regionalDecision = resolveRegionalPolicy({country:country, region:region, source:geoSource});
    if (choiceRevision !== bootRevision) return; // A newer explicit choice takes priority.
    if (choice || privacySignal()) {
      apply(choice === 'granted', choice ? 'stored-' + choice : 'privacy-signal'); banner(showRefusalBanner());
      if (choice === 'denied' && choiceRecord && choiceRecord.scope === 'pending-region') {
        var pending = choiceRecord, revision = choiceRevision; locationReady().then(function () { settleRefusal(pending,revision); });
      }
      return;
    }
    await locationReady();
    if (choice) return; // Never let late geography overwrite a click.
    var auto = regionalDecision.regime === 'automatic' && regionalDecision.ga4 === 'cookies';
    if (auto && !canRememberVisit()) { apply(false,'preference-storage-unavailable'); banner(false); return; }
    apply(auto, 'regional-policy');
    banner(regionalDecision.banner);
  }
  function keepVisitActive() {
    if (choice !== 'denied' || !choiceRecord || choiceRecord.scope !== 'visit') return;
    var elapsed=Date.now() - choiceRecord.lastSeen;
    if (elapsed < 30000 || elapsed >= visitIdle) return;
    choiceRecord=Object.assign({},choiceRecord,{lastSeen:Date.now()}); saveVisit(choiceRecord);
  }
  if (w.addEventListener) {
    w.addEventListener('scroll',keepVisitActive,{passive:true});
    w.addEventListener('pointerdown',keepVisitActive,{passive:true});
    w.addEventListener('keydown',keepVisitActive);
    w.addEventListener('storage', function (event) {
      if (event.key !== key + '_signal' || !event.newValue) return;
      var record=fromJSON(event.newValue); if (!valid(record) || (choiceRecord && (record.at < choiceRecord.at || (record.at === choiceRecord.at && record.analytics === choiceRecord.analytics)))) return;
      choiceRevision++; choice=record.analytics; choiceRecord=record;
      if (choice === 'denied') saveVisit(record);
      apply(choice === 'granted','shared-explicit-' + choice); banner(false);
    });
    w.addEventListener('focus', function () {
      var remembered=stored();
      if (remembered === 'denied') { choiceRevision++; choice='denied'; apply(false,'stored-denied'); }
      else if (remembered === 'granted') { choiceRevision++; choice='granted'; apply(true,'stored-granted'); banner(false); }
    });
  }
  w.MAConsent = {acceptAnalytics: function () { choose('granted'); }, rejectAll: function () { choose('denied'); }, openSettings: function () { banner(true); }, state: function () { return {country: country, region: region, geoSource: geoSource, regionalRegime:regionalDecision.regime, regionalRule:regionalDecision.rule, choiceScope: choiceRecord && choiceRecord.scope, choiceExpiresAt: choiceRecord && choiceRecord.expiresAt, mode: mode, loaded: loaded, pageViewSent: sent, analytics: !w[disabled] && mode !== 'cookieless-denied-storage', measurementEnabled: !w[disabled], advertising: false}; }};
  if (d.readyState === 'loading') w.MAConsent.ready = new Promise(function (resolve) { d.addEventListener('DOMContentLoaded', function () { boot().then(resolve); }, {once: true}); });
  else w.MAConsent.ready = boot();
})(window, document);

