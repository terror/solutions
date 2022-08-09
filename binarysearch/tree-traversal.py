class Solution:
  def solve(self, root, moves):
    par = []
    for move in moves:
      if move == 'RIGHT':
        par.append(root)
        root = root.right
      elif move == 'LEFT':
        par.append(root)
        root = root.left
      else:
        root = par.pop()
    return root.va
