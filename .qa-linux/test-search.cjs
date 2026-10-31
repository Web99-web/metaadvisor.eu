const fs=require('fs'),path=require('path'),assert=require('assert'),{performance}=require('perf_hooks');
const O=process.env.MA_QA_OUTPUT, engine=require(path.join(process.cwd(),'static/js/article-search.js'));
const tests=[],measurements=[],languages=[['en',''],['hr','hr/'],['de','de/']];
function check(name,fn){fn();tests.push(name);}
const fixtures=engine.prepare([
 {title:'Metaplanet MetaMask metadata metaverse MetaAdvisor',summary:'',tags:[],content:''},
 {title:'Domain blockchain failure',summary:'said chain',tags:[],content:''},
 {title:'Sold insolvent consolidation',summary:'method Tether',tags:[],content:''},
 {title:'Meta Platforms account suspensions',summary:'Facebook disabled accounts and AI moderation',tags:['meta'],content:'Meta Oversight Board'},
 {title:'Bitcoin Ethereum Solana',summary:'',tags:[],content:''},
 {title:'Unrelated bank announcement',summary:'Interest rates',tags:[],content:'Follow us on Facebook.'},
 {title:'Kripto profili na X-u i kriva meta',summary:'',tags:[],content:'Nothing about Meta Platforms.'},
 {title:'Facebook group warns of Booking phishing',summary:'Booking hotel scam',tags:[],content:'Facebook group discusses hotels.'},
 {title:'Unrelated URL',summary:'',tags:[],content:'https://metaadvisor.eu/news/sol-btc-eth-ai-meta/'}
]);
for(const q of ['Meta','AI','AI moderation','disabled accounts'])check('whole words and entity '+q,()=>assert.deepStrictEqual(engine.search(fixtures,q).map(x=>x.row.title),['Meta Platforms account suspensions']));
for(const q of ['BTC','ETH','SOL'])check('controlled alias '+q,()=>assert.deepStrictEqual(engine.search(fixtures,q).map(x=>x.row.title),['Bitcoin Ethereum Solana']));
check('all words required',()=>assert.strictEqual(engine.search(fixtures,'AI nonexistentword').length,0));
check('Unicode whole word',()=>assert.deepStrictEqual(engine.tokens('ŽALBE $ETH ETH/USD'),['zalbe','eth','eth','usd']));
const languagesResult={};
for(const [lang,prefix] of languages){
 const raw=JSON.parse(fs.readFileSync(path.join(O,'public',prefix,'index.json'),'utf8'));
 let t=performance.now();const docs=engine.prepare(raw);const init=performance.now()-t;
 const queries=['Meta','Facebook','AI moderation','disabled accounts','BTC','ETH','SOL','20 milijuna','20 million','20 millionen'];
 const result={articles:raw.length,prepare_ms:init,queries:{}};
 check(lang+' AI KI identical results and ranking',()=>assert.deepStrictEqual(engine.search(docs,'AI').map(x=>x.row.url),engine.search(docs,'KI').map(x=>x.row.url))); 
 for(const q of queries){
  t=performance.now();const found=engine.search(docs,q);const ms=performance.now()-t;
  result.queries[q]={total:found.length,ms,first:found.slice(0,3).map(x=>({title:x.row.title,url:x.row.url})),account20m_position:found.findIndex(x=>/20-million|20-milijun/.test(x.row.url))+1};
  check(lang+' query '+q,()=>{assert(found.every(x=>x.score>0));assert.strictEqual(new Set(found.map(x=>x.row.url)).size,found.length);});
 }
 for(const q of ['Meta','Facebook','AI moderation','disabled accounts'])check(lang+' 20m searchable '+q,()=>assert(result.queries[q].account20m_position>0,JSON.stringify(result.queries[q])));
 const localized=lang==='hr'?['AI moderacija','blokirani računi','20 milijuna']:lang==='de'?['KI-Moderation','gesperrte Konten','20 Millionen']:['AI moderation','disabled accounts','20 million'];
 for(const q of localized)check(lang+' localized '+q,()=>assert(engine.search(docs,q).some(x=>/20-million|20-milijun/.test(x.row.url))));
 check(lang+' EU appeals discoverable by entity context',()=>assert(engine.search(docs,'Meta').some(x=>/eu-appeals|eu-.*zalbe|eu-.*beschwerden/.test(x.row.url))));
 for(const q of ['Meta','AI','ETH','BTC','SOL']){
  const hits=engine.search(docs,q);if(q==='Meta')check(lang+' no unrelated title-only brands',()=>assert(!hits.some(x=>/^(Metaplanet|MetaMask)/i.test(x.row.title))));
 }
 const numbered=engine.search(docs,'Facebook');
 check(lang+' all results accessible beyond 30',()=>{assert(numbered.length>30);const pages=[];for(let i=0;i<numbered.length;i+=30)pages.push(...numbered.slice(i,i+30));assert.strictEqual(pages.length,numbered.length);});
 const escaped=raw.filter(x=>/\{\{[<%]|class="support|SECRETSUPPORT|SECRETADTOKEN/.test(x.content));check(lang+' cleaned article content',()=>assert.strictEqual(escaped.length,0));
 check(lang+' no article body erased by boilerplate removal',()=>assert(!raw.some(x=>x.content.trim().length<50)));
 check(lang+' legacy ANDY article body preserved',()=>assert(raw.find(x=>/andy-eth-friend/.test(x.url)).content.length>1000));
 languagesResult[lang]=result;
}
fs.writeFileSync(path.join(O,'SEARCH-TESTS.json'),JSON.stringify({PASS:true,tests:tests.length,languages:languagesResult,memory:process.memoryUsage()},null,2));console.log('PASS',tests.length,JSON.stringify(languagesResult));
