import sys,unittest,tempfile,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from release_articles import load_release_articles, article_membership_preserved
from finalize_release import Policy
D='https://metaadvisor.eu'
class Guards(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent);self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)/'src';self.out=Path(self.tmp.name)/'out';(self.root/'migration').mkdir(parents=True);(self.root/'data').mkdir();self.old=[];self.rows={}
  for lang,prefix in [('en',''),('de','/de'),('hr','/hr')]:
   urls=[prefix+'/news/old/',prefix+'/news/new/'];self.rows[lang]=[{'url':u,'title':'Article','content':'Real article body'} for u in urls];self.old.append({'url':D+urls[0],'lang':lang})
   for u in urls:
    f=self.out/u.strip('/')/'index.html';f.parent.mkdir(parents=True,exist_ok=True);f.write_text('<html/>')
  (self.root/'migration/expected-primary-pages.json').write_text(json.dumps(self.old));(self.root/'data/article_routes.json').write_text(json.dumps({'aliases':{D+'/news/old-alias/':D+'/news/old/'}}));self.save()
 def save(self):
  for lang,rows in self.rows.items():
   q=self.out/('' if lang=='en' else lang);q.mkdir(parents=True,exist_ok=True);(q/'index.json').write_text(json.dumps(rows));s=self.out/lang;s.mkdir(exist_ok=True);(s/'sitemap.xml').write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+D+r['url']+'</loc></url>' for r in rows)+'</urlset>')
 def rejected(self):
  self.save()
  with self.assertRaises(ValueError):load_release_articles(self.root,self.out)
 def test_new_triplet_allowed(self):self.assertEqual(len(load_release_articles(self.root,self.out)),6)
 def test_archive_accepts_new_article(self):self.assertTrue(article_membership_preserved({'old','new'},{'old'},{'new'}))
 def test_archive_cannot_lose_old_article(self):self.assertFalse(article_membership_preserved({'new'},{'old'},{'new'}))
 def test_archive_cannot_gain_unapproved_old_member(self):self.assertFalse(article_membership_preserved({'old','unrelated-old'},{'old'},{'new'}))
 def test_archive_cannot_gain_alias(self):self.assertFalse(article_membership_preserved({'old','alias'},{'old'},{'new'}))
 def test_historical_loss_rejected(self):self.rows['en']=self.rows['en'][1:];self.rejected()
 def test_duplicate_rejected(self):self.rows['en'].append(self.rows['en'][0]);self.rejected()
 def test_archive_rejected(self):self.rows['en'][1]['url']='/tags/ai/';self.rejected()
 def test_pagination_rejected(self):self.rows['en'][1]['url']='/news/page/2/';self.rejected()
 def test_language_overlap_rejected(self):self.rows['de'][1]['url']='/news/new/';self.rejected()
 def test_alias_rejected(self):self.rows['en'][1]['url']='/news/old-alias/';self.rejected()
 def test_external_rejected(self):self.rows['en'][1]['url']='//other.example/news/new/';self.rejected()
 def test_encoded_separator_rejected(self):self.rows['en'][1]['url']='/news/unsafe%2Fname/';self.rejected()
 def test_missing_html_rejected(self):
  (self.out/'de/news/new/index.html').unlink()
  with self.assertRaises(ValueError):load_release_articles(self.root,self.out)
 def test_sitemap_disagreement_rejected(self):
  (self.out/'hr/sitemap.xml').write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>')
  with self.assertRaises(ValueError):load_release_articles(self.root,self.out)
 def test_new_article_keeps_index_and_hreflang(self):
  raw='<html><head><meta name="robots" content="index,follow"><link rel="alternate" hreflang="de" href="'+D+'/de/news/new/"></head></html>';x=Policy(raw,D+'/news/new/',True,{});x.feed(raw);self.assertEqual(x.result(),raw)
 def test_auxiliary_stays_noindex(self):
  raw='<html><head><link rel="alternate" hreflang="de" href="'+D+'/de/tags/ai/"></head></html>';x=Policy(raw,D+'/tags/ai/',False,{});x.feed(raw);out=x.result();self.assertIn('noindex',out);self.assertNotIn('hreflang',out)
if __name__=='__main__':unittest.main(verbosity=2)


