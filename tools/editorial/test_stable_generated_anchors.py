import unittest
from stable_generated_anchors import normalize_bytes
class Anchors(unittest.TestCase):
 def test_restores_original_identifiers_and_self_links_only(self):
  raw=b'<title>Same</title><h2 id=hahahugoshortcode3043s1hbhb>Same text</h2><a href=#hahahugoshortcode3043s1hbhb>Go</a>'
  wanted=raw.replace(b'hahahugoshortcode3043s1hbhb',b'hahahugoshortcode3048s1hbhb');self.assertEqual(normalize_bytes('page',raw,{'page':['hahahugoshortcode3048s1hbhb']}),(wanted,1))
 def test_unknown_anchor_blocks(self):
  with self.assertRaises(ValueError):normalize_bytes('page',b'<h2 id=hahahugoshortcode3s1hbhb>Text</h2>',{})
 def test_missing_protected_anchor_blocks(self):
  with self.assertRaises(ValueError):normalize_bytes('page',b'<h2 id=changed>Text</h2>',{'page':['hahahugoshortcode3048s1hbhb']})
 def test_order_change_blocks(self):
  with self.assertRaises(AssertionError):normalize_bytes('page',b'<h2 id=hahahugoshortcode3s2hbhb>Text</h2>',{'page':['hahahugoshortcode3048s1hbhb']})
if __name__=='__main__':unittest.main()
