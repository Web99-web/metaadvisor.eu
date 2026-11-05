// Optional first-party geography only. No IP, cookie, logging or third-party calls.
export function regionData(request) {
  const cf=request.cf || {},country=/^[A-Z]{2}$/.test(cf.country || '') && cf.country!=='XX'?cf.country:'UNKNOWN';
  const region=/^[A-Z0-9]{1,3}$/.test(cf.regionCode || '')?cf.regionCode:'';
  return {schema:1,country,region};
}
export function regionResponse(request) {
  return new Response(request.method==='HEAD'?null:JSON.stringify(regionData(request)),{status:200,headers:{'Content-Type':'application/json; charset=utf-8','Cache-Control':'private, no-store','X-Robots-Tag':'noindex'}});
}
