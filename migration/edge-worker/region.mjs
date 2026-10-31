// Optional first-party geography only. No IP, cookie, logging or third-party calls.
export function regionResponse(request) {
  const cf=request.cf || {},country=/^[A-Z]{2}$/.test(cf.country || '')?cf.country:'UNKNOWN';
  const region=/^[A-Z0-9]{1,3}$/.test(cf.regionCode || '')?cf.regionCode:'';
  return new Response(request.method==='HEAD'?null:JSON.stringify({schema:1,country,region}),{status:200,headers:{'Content-Type':'application/json; charset=utf-8','Cache-Control':'private, no-store','X-Robots-Tag':'noindex'}});
}
