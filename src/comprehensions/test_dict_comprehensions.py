import unittest

class DictComprehensionTests(unittest.TestCase):

  def test_dict_comprehensions_copy_dict(self):
    d = {'one': 1, 'two': 2, 'three': 3}
    comp = {k:v for (k,v) in d.items()}
    self.assertEquals(d, comp)
    self.assertFalse(d is comp)



if __name__ == '__main__':
  unittest.main()
