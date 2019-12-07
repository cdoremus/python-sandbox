import unittest
import collections

class TestGeneratorExpressions(unittest.TestCase):

  def test_generator_exp_iterator(self):
    rng = range(10)
    gen_exp = (i for i in rng)
    # NOTE: generator expressions create an iterator
    self.assertIsInstance(gen_exp, collections.Iterator)
    count = 0 # range starts at zero
    for x in gen_exp:
      self.assertEqual(x, count)
      count = count + 1


if __name__ == '__main__':
  unittest.main()