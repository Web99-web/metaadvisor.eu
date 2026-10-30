import {regionResponse} from './region.mjs';
import redirects from './redirects.mjs';
function pathKey(path) {
  try { return path.split('/').map(p => encodeURIComponent(decodeURIComponent(p)).replace(/[!'()*]/g, c => '%' + c.charCodeAt(0).toString(16).toUpperCase())).join('/'); }
  catch (_) { return null; }
}
export async function handle(request, upstream = fetch) {
  const u = new URL(request.url);
  if (u.hostname !== 'metaadvisor.eu') return upstream(request);
  if (u.pathname === '/_ma/region' && (request.method === 'GET' || request.method === 'HEAD')) return regionResponse(request);
  const key = pathKey(u.pathname), target = key && redirects[key];
  if (target && (request.method === 'GET' || request.method === 'HEAD')) {
    const t = new URL(target); if (!t.search) t.search = u.search;
    return new Response(null, {status: 301, headers: {Location: t.href, 'Cache-Control': 'public, max-age=3600'}});
  }
  const response = await upstream(request);
  if (/\/index\.xml$/.test(u.pathname) && response.status === 200) {
    const headers = new Headers(response.headers); headers.set('X-Robots-Tag', 'noindex, follow');
    return new Response(response.body, {status: response.status, statusText: response.statusText, headers});
  }
  return response;
}
export default {fetch(request) { return handle(request); }};
