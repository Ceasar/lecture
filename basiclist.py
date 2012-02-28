"""Representaiton of BasicList class."""


class BasicList(object):
  """A simplified list.

  >>> x = BasicList()
  >>> x
  []
  >>> x.append(1)
  >>> x
  [1]
  >>> x.append(0)
  >>> x
  [1, 0]
  >>> x[0] = 5
  >>> x
  [5, 0]
  >>> x.extend([-1, 500, 7])
  >>> x
  [5, 0, -1, 500, 7]
  """

  def __init__(self):
    self._data = []

  def append(self, value):
    """Add a value to the end of the list."""
    self._data.append(value)

  def extend(self, value):
    """Extend the list by the given sequence."""
    self._data.extend(value)

  def __getitem__(self, index):
    return self._data[index]

  def __setitem__(self, index, value):
    self._data[index] = value
  
  def __iter__(self):
    for item in self._data:
      yield item
  
  def __len__(self):
    return len(self._data)

  def __str__(self):
    return str(self._data)

  def __repr__(self):
    return repr(self._data)


if __name__ == "__main__":
  import doctest
  doctest.testmod()
