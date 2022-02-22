# First start by sorting all interval pairs (end, start).
#
# Iterate through each pair keeping track of a running max ending time.
#
# If we encounter a starting time greater than or equal to this running max
# ending time, increase the answer.
#
# The main idea is to acknowledge the fact that if the next intervals starting time is greater
# than or equal to the current intervals ending time, it does not overlap with our current interval. This only
# works if the intervals are sorted according to their ending times because we cannot use this method of
# comparison for a pair of intervals that is flipped chronologically (i.e first comes after the second).
#
# 1 4
# 2 8 --> [I(e=4, s=1), I(e=8, s=2), I(e=9, s=5)]
# 5 9
#
#  ----
#   -------
#      -----
#  ^   ^
# (The points that contribute to our answer)

from collections import namedtuple

I = namedtuple('I', 'e s')

def main(intervals):
  S = 0
  A = 0
  for interval in intervals:
    if interval.s >= S:
      S = interval.e
      A += 1
  return A

if __name__ == '__main__':
  print(main(sorted([I(*reversed(list(map(int, input().split())))) for _ in range(int(input()))])))
