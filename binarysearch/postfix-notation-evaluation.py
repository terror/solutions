class Solution:
  def solve(self, exp):
    s, o = [], {
      '+': lambda a, b: a + b,
      '-': lambda a, b: a - b,
      '*': lambda a, b: a * b,
      '/': lambda a, b: a / b,
    }

    for op in exp:
      if op.lstrip('-').isdigit():
        s.append(int(op))
      else:
        a, b = s.pop(), s.pop()
        r = o[op](b, a)
        s.append((ceil(r), floor(r))[r > 0])

    return s[-1]
