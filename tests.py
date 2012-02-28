import string
import random
import unittest

from sortedlist import SortedList

random.seed(0)


class SortedListTestCase(unittest.TestCase):
  def setUp(self):
    self.sorted_list = SortedList()

  @property
  def is_sorted(self):
    for i, item in enumerate(self.sorted_list):
      if i == 0:
        current = item
      else:
        if current > item:
          return False
    return True

  def test_append_is_sorted(self):
    items = []
    for _ in xrange(200):
      num = random.uniform(-100, 100)
      self.sorted_list.append(num)
      self.assertTrue(self.is_sorted)

  def test_append_keeps_items(self):
    items = []
    for _ in xrange(200):
      num = random.uniform(-100, 100)
      self.sorted_list.append(num)
      items.append(num)
      items.sort()
      for i, j in zip(items, self.sorted_list):
        self.assertEqual(i, j)

  def test_extend_is_sorted(self):
    nums = range(-100, 100)
    random.shuffle(nums)
    self.sorted_list.extend(nums)
    self.assertTrue(self.is_sorted)

  def test_extend_keeps_items(self):
    nums = range(-100, 100)
    random.shuffle(nums)
    self.sorted_list.extend(nums)
    nums.sort()
    for i, j in zip(nums, self.sorted_list):
      self.assertEqual(i, j)

  def test_setitem_is_sorted(self):
    nums = xrange(-100, 100)
    self.sorted_list.extend(nums)

    for _ in xrange(200):
      self.sorted_list[random.randint(0, len(self.sorted_list) - 1)] = random.uniform(-100, 100)
      self.assertTrue(self.is_sorted)

  def test_setitem_keeps_items(self):
    nums = range(-100, 100)
    self.sorted_list.extend(nums)

    for _ in xrange(200):
      index = random.randint(0, len(self.sorted_list) - 1)
      num = random.uniform(-100, 100)
      self.sorted_list[index] = num
      nums[index] = num
      nums.sort()
      for i, j in zip(self.sorted_list, nums):
        self.assertEqual(i, j)


if __name__ == "__main__":
    unittest.main()
