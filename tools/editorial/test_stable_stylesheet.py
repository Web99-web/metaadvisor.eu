import unittest
from stable_stylesheet import normalize_bytes
class Stable(unittest.TestCase):
 def test_only_css_cache_key_changes(self):
  raw=b'<title>Title</title><link rel=canonical href="https://example.invalid/?v=123"><link rel=stylesheet href="/css/style.css?v=1793521216"><p>Text</p><img src="/x.png?v=123">'
  expected=raw.replace(b'/css/style.css?v=1793521216',b'/css/style.css?v=abcdef1234567890abcd');self.assertEqual(normalize_bytes(raw,'abcdef1234567890abcd'),(expected,1))
 def test_idempotent(self):
  raw=b'<link rel=stylesheet href="/css/style.css?v=abcdef1234567890abcd">';self.assertEqual(normalize_bytes(raw,'abcdef1234567890abcd'),(raw,1))
 def test_unknown_query_refused(self):
  with self.assertRaises(ValueError):normalize_bytes(b'<link rel=stylesheet href="/css/style.css?unknown=123">','abcdef1234567890abcd')
 def test_non_stylesheet_untouched(self):
  raw=b'<a href="/css/style.css?v=123">Read</a>';self.assertEqual(normalize_bytes(raw,'abcdef1234567890abcd'),(raw,0))
 def test_invalid_digest_refused(self):
  with self.assertRaises(ValueError):normalize_bytes(b'', 'timestamp')
if __name__=='__main__':unittest.main()
