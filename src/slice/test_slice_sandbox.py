import unittest

class TestSlice(unittest.TestCase):

  def test_slice_with_end(self):
    arr = [1,2,3,4,5,6]
    start = 2
    end = 4
    exp = [3,4]
    ans = arr[start:end]
    self.assertEqual(exp, ans)

  def test_slice_no_end(self):
    arr = [1,2,3,4,5,6]
    start = 2
    exp = [3,4,5,6]
    ans = arr[start:]
    self.assertEqual(exp, ans)


  def test_slice_with_start_past_end(self):
    arr = [1,2,3,4,5,6]
    start = 12
    exp = []
    ans = arr[start:]
    self.assertEqual(exp, ans)

  def test_slice_empty_list(self):
    arr = []
    start = 0
    exp = []
    ans = arr[0:]
    self.assertEqual(exp, ans)


  def test_slice_to_copy(self):
    arr = [1,2,3,4,5,6]
    exp = arr
    ans = arr[:]
    self.assertEqual(exp, ans)

if __name__ == '__main__':
  unittest.main()
