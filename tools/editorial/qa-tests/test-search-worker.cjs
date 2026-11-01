const fs=require('fs'),path=require('path'),assert=require('assert'),http=require('http'),{Worker}=require('worker_threads');
const O=process.env.MA_QA_OUTPUT,P=path.join(O,'public'),source=fs.readFileSync('static/js/article-search.js','utf8'),requests=[];
const server=http.createServer((req,res)=>{requests.push(req.url);const f=path.resolve(P,'.'+req.url);if(!f.startsWith(P+path.sep)||!fs.existsSync(f)){res.statusCode=404;return res.end();}res.setHeader('Content-Type',req.url.endsWith('.json')?'application/json':'text/javascript');fs.createReadStream(f).pipe(res);});
(async()=>{await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin='http://127.0.0.1:'+server.address().port,results=[];let worker;
try{for(const lang of ['en','hr','de']){
 const start=requests.length;worker=new Worker(`const {parentPort,workerData}=require('worker_threads');const vm=require('vm');const self={postMessage:m=>parentPort.postMessage(m)};vm.runInNewContext(workerData.source,{self,fetch:(url,opt)=>fetch(new URL(url,workerData.origin),opt),URL,console});parentPort.on('message',m=>self.onmessage({data:m}));`,{eval:true,workerData:{source,origin}});
 const ask=m=>new Promise((resolve,reject)=>{const fail=e=>reject(e);const timer=setTimeout(()=>{worker.off('error',fail);reject(Error('Worker timeout'));},20000);worker.once('message',r=>{clearTimeout(timer);worker.off('error',fail);resolve(r)});worker.once('error',fail);worker.postMessage(m)});
 assert.strictEqual(requests.length,start);const index=(lang==='en'?'':'/'+lang)+'/index.json';let id=0;
 for(const q of ['Meta','Facebook','AI moderation','disabled accounts','AI','KI','BTC','ETH','SOL']){const r=await ask({id:++id,path:index,query:q,page:0});assert(!r.error&&r.total>0&&r.rows.length===Math.min(30,r.total));}
 let r=await ask({id:++id,path:index,query:'Facebook',page:0});const first=r.rows[0].url,total=r.total;assert(total>30);
 r=await ask({id:++id,path:index,query:'Facebook',page:1});assert(r.page===1&&r.total===total&&r.rows[0].url!==first);
 r=await ask({id:++id,path:index,query:'Facebook',page:Math.ceil(total/30)-1});assert(r.page===Math.ceil(total/30)-1&&r.rows.length>0);
 r=await ask({id:++id,path:index,query:'unfindablezzzzz',page:0});assert(r.total===0&&r.rows.length===0);
 assert.deepStrictEqual(requests.slice(start),[index]);await worker.terminate();worker=null;results.push({lang,PASS:true,index_requests:1,queries:9,pagination_to_final_page:true});
}fs.writeFileSync(path.join(O,'SEARCH-WORKER-TESTS.json'),JSON.stringify({PASS:true,platform:process.platform,results,external_requests:0},null,2));console.log(JSON.stringify(results));}
finally{if(worker)await worker.terminate();server.close();}})().catch(e=>{console.error(e);process.exitCode=1;server.close();});
