import unittest
from slice_sandbox import sliceList

class TestSlice(unittest.TestCase):

  def test_slice_with_end(self):
    arr = [1,2,3,4,5,6]
    start = 2
    end = 4
    exp = [3,4]
    ans = sliceList(arr, start, end)
    self.assertEqual(exp, ans)

  def test_slice_no_end(self):
    arr = [1,2,3,4,5,6]
    start = 2
    exp = [3,4,5,6]
    ans = sliceList(arr, start)
    self.assertEqual(exp, ans)


  def test_slice_with_start_past_end(self):
    arr = [1,2,3,4,5,6]
    start = 12
    exp = []
    ans = sliceList(arr, start)
    self.assertEqual(exp, ans)

  def test_slice_empty_list_with_start_past_end(self):
    arr = []
    start = 0
    exp = []
    ans = sliceList(arr, start)
    self.assertEqual(exp, ans)

  def test_slice_with_no_start_or_end(self):
    arr = [1,2,3,4,5,6]
    exp = arr
    ans = sliceList(arr)
    self.assertEqual(exp, ans)

if __name__ == '__main__':
  unittest.main()