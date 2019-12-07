import unittest

class SetComprehensions(unittest.TestCase):

  def test_set_remove_dups(self):
    s1 = {1, 2, 2, 3}
    self.assertTrue(s1 == {1,2,3})

  def test_set_comprehensions(self):
    s1 = {1, 2, 2, 3}
    exp = {1, 2, 3}
    ans ={c for c in s1}
    self.assertEqual(exp, ans)

  def test_set_comprehensions_with_conditional(self):
    s1 = {1, 2, 2, 3}
    exp = {1, 3}
    ans ={c for c in s1 if c % 2 != 0}
    self.assertEqual(exp, ans)

if __name__ == '__main__':
  unittest.main()