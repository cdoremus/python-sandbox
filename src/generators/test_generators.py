import unittest
import types

class TestGenerators(unittest.TestCase):

  def test_generator_yield_single_value(self):
    exp = 1
    def gen1():
      yield exp
    ans = gen1()
    self.assertIsInstance(ans, types.GeneratorType)
    self.assertEqual(next(ans), exp)

  def test_generator_yield_single_value_next_called_twice(self):
    exp = 2
    def gen1():
      yield exp
    ans = gen1()
    self.assertEqual(next(ans), exp)
    with self.assertRaises(StopIteration):
      next(ans)

  def test_generator_yield_from_iteration(self):
    arr = [1, 2, 3, 4]
    def gen1(seq):
      for i in seq:
        yield i
    ans = gen1(arr)
    self.assertEqual(next(ans), arr[0])
    self.assertEqual(next(ans), arr[1])
    self.assertEqual(next(ans), arr[2])
    self.assertEqual(next(ans), arr[3])
    with self.assertRaises(StopIteration):
      next(ans)

if __name__ == '__main__':
  unittest.main()