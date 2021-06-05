def main(l):
  try:    print(sorted(list(filter(lambda x: len(x) == min([len(w) for w in l]), l)))[-1])
  except: print("neibb!")

if __name__ == '__main__':
  main(list(filter(lambda x: len(x) >= 5 and len(set(x)) == len(x), [input() for _ in range(int(input()))])))
