import unittest

class DictComprehensionTests(unittest.TestCase):

  def test_dict_comprehensions_copy_dict(self):
    d = {'one': 1, 'two': 2, 'three': 3}
    comp = {k:v for (k,v) in d.items()}
    self.assertEqual(d, comp)
    self.assertFalse(d is comp)

  def test_dict_comprehensions_filtering(self):
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
    comp = {k:v for (k,v) in d.items() if v % 2 == 0}
    self.assertEqual({'two': 2, 'four': 4}, comp)


if __name__ == '__main__':
  unittest.main()
