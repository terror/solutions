class Solution:
  def solve(self, tasks, people):
    tasks.sort()
    people.sort()

    j = 0
    for i, v in enumerate(people):
      if j == len(tasks):
        break
      if v < tasks[j]:
        continue
      j += 1

    return j
