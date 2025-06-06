class Vector2D:
  def __init__(self, vec: list[list[int]]):
    self.vec = []
    self.i = 0

    for arr in vec:
      self.vec += arr

  def next(self) -> int:
    ans = self.vec[self.i]
    self.i += 1
    return ans

  def hasNext(self) -> bool:
    return self.i < len(self.vec)
