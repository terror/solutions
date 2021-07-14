"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
  def __init__(self):
    self.d = collections.defaultdict(list)
    self.val = {}
    self.ans = 0
    self.vis = [0] * int(2e5)

  def getImportance(self, employees: List['Employee'], id: int) -> int:
    for i in range(len(employees)):
      eid, imp, sub = employees[i].id, employees[i].importance, employees[i].subordinates
      self.d[eid] = sub
      self.val[eid] = imp

    self.dfs(id)
    return self.ans

  def dfs(self, v):
    self.vis[v] = 1
    self.ans += self.val[v]
    for u in self.d[v]:
      if not self.vis[u]:
        self.vis[u] = 1
        self.dfs(u)
