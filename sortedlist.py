from basiclist import BasicList


class SortedList(BasicList):
  """A sorted, simplified list class.
  >>> y = SortedList()
  >>> y
  []
  >>> y.append(1)
  >>> y
  [1]
  >>> y.append(0)
  >>> y
  [0, 1]
  >>> y[0] = 5
  >>> y
  [1, 5]
  >>> y.extend([-1, 500, 7])
  >>> y
  [-1, 1, 5, 7, 500]
  """
  
  def append(self, value):
    """Add an item to the end of the list."""
    super(SortedList, self).append(value)
    self._data.sort()

  def extend(self, values):
    """Add the contents of a list to this list."""
    super(SortedList, self).extend(values)
    self._data.sort()

  def __setitem__(self, index, value):
    super(SortedList, self).__setitem__(index, value)
    self._data.sort()


if __name__ == "__main__":
  import doctest
  doctest.testmod()
