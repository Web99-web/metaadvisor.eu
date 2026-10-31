"""Current Hugo articles, with the frozen migration inventory as a minimum guard.

Read two independently rendered outputs: the news-only search indexes and the
language sitemaps. Never extend or rewrite the historical migration approvals.
"""
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

from migration_gate import key

DOMAIN = 'https://metaadvisor.eu'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}


def article_membership_preserved(current, historical, new_articles):
    """Keep every approved member; only current newly published articles may join."""
    return historical <= current and current - historical <= new_articles


def article_key(url, language, historical):
    normalized = key(url)
    path = urlsplit(normalized).path
    # Some approved historical articles have custom URLs outside /news/.
    # Preserve those exact routes without opening archive paths to new entries.
    if normalized in historical:
        if historical[normalized]['lang'] != language:
            raise ValueError('Historical article language changed: ' + url)
        return normalized
    prefix = '/news/' if language == 'en' else '/' + language + '/news/'
    if not path.startswith(prefix) or not path.endswith('/'):
        raise ValueError('Not a regular article URL: ' + url)
    tail = path[len(prefix):].strip('/')
    if (not tail or re.match(r'^page/\d+(?:/|$)', tail)
            or re.search(r'%(?:2f|5c|00)', path, re.I)):
        raise ValueError('Archive or unsafe article URL: ' + url)
    return normalized


def article_file(output, url):
    parts = unquote(urlsplit(url).path).strip('/').split('/')
    if os.name == 'nt':
        parts = [p.rstrip('. ') for p in parts]
    target = output.joinpath(*parts, 'index.html')
    if not target.resolve().is_relative_to(output.resolve()):
        raise ValueError('Article path escapes build output: ' + url)
    return target


def load_release_articles(root, output):
    """Fail closed on aliases, archives, duplicates, missing history or XML drift."""
    root, output = Path(root), Path(output)
    baseline = json.loads((root / 'migration/expected-primary-pages.json').read_text(encoding='utf-8'))
    historical = {key(r['url']): r for r in baseline}
    if len(historical) != len(baseline):
        raise ValueError('Duplicate historical primary URL')
    aliases = {key(u) for u in json.loads((root / 'data/article_routes.json').read_text(encoding='utf-8'))['aliases']}
    articles, sitemap = {}, {}
    for lang in ('en', 'de', 'hr'):
        index = output / ('' if lang == 'en' else lang) / 'index.json'
        rows = json.loads(index.read_text(encoding='utf-8'))
        if not isinstance(rows, list) or not rows:
            raise ValueError('Missing current article index: ' + lang)
        for row in rows:
            relative = row.get('url', '')
            if not isinstance(relative, str) or not relative.startswith('/') or relative.startswith('//'):
                raise ValueError('Invalid search article URL')
            url = DOMAIN + relative
            k = article_key(url, lang, historical)
            if k in articles or k in aliases:
                raise ValueError('Duplicate or migrated alias in article index: ' + url)
            if not all(isinstance(row.get(f), str) and row[f].strip() for f in ('title', 'content')):
                raise ValueError('Not an article search record: ' + url)
            if not article_file(output, url).is_file():
                raise ValueError('Current article HTML missing: ' + url)
            articles[k] = {'url': url, 'lang': lang, 'kind': 'page', 'section': 'news', 'title': row['title']}
        tree = ET.parse(output / lang / 'sitemap.xml').getroot()
        if tree.tag != '{' + NS['s'] + '}urlset':
            raise ValueError('Unexpected language sitemap root: ' + lang)
        for node in tree.findall('s:url', NS):
            url = node.findtext('s:loc', namespaces=NS)
            k = article_key(url or '', lang, historical)
            if k in sitemap or k in aliases:
                raise ValueError('Duplicate or migrated alias in sitemap: ' + str(url))
            sitemap[k] = lang
    if not set(historical).issubset(articles):
        raise ValueError('Historical articles disappeared: ' + repr(sorted(historical.keys() - articles.keys())[:10]))
    if set(sitemap) != set(articles) or any(sitemap[k] != r['lang'] for k, r in articles.items()):
        raise ValueError('Current article index/sitemap disagree')
    return list(articles.values())
