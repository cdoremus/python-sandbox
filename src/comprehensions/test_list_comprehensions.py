import unittest

class ListComprehensionTests(unittest.TestCase):

  def setUp(self):
    pass

  def test_simple_list_comprehension(self):
    lst = [1,2,3,4,5]
    comp = [i for i in lst]
    for c in comp:
      self.assertTrue(c in lst)
    self.assertEquals(lst,comp)
    self.assertFalse(lst is comp)


  def test_filtered_list_comprehension(self):
    lst = [1,2,3,4,5]
    exp = [2,4]
    comp = [i for i in lst if i % 2 == 0]
    self.assertEquals(exp,comp)

  def test_filtered_and_modified_list_comprehension(self):
    lst = [1,2,3,4,5]
    exp = [4,16]
    comp = [i*i for i in lst if i % 2 == 0]
    self.assertEquals(exp,comp)

  def test_filtered_and_type_modified_list_comprehension(self):
    lst = [1,2,3,4,5]
    exp = ['2', '4']
    comp = [str(i) for i in lst if i % 2 == 0]
    self.assertEquals(exp,comp)

  def test_nested_list_comprehension(self):
    lst1 = [1,2,3,4,5,6]
    lst2 = [4,5,6,7,8]
    ans = [i for i in lst1 if i in lst2]
    self.assertEquals([4,5,6], ans)


if __name__ == '__main__':
  unittest.main()
