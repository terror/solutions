def main(s):
  return s.index('(') == (len(s) - 1 - s.index(')'))

if __name__ == '__main__':
  print('correct' if main(input()) else 'fix')
