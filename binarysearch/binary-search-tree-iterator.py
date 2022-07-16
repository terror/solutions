# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root):
      self.arr = self.__build(root, [])
      self.pointer = 0

    def next(self):
      t = self.arr[self.pointer]
      self.pointer += 1
      return t

    def hasnext(self):
      return len(self.arr) > self.pointer

    def __build(self, root, arr):
      if not root:
        return []
      if root.left:
        self.__build(root.left, arr)
      arr.append(root.val)
      if root.right:
        self.__build(root.right, arr)
      return arr
