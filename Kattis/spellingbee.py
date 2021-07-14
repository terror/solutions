def main():
  h = list(input())
  for _ in range(int(input())):
    x = list(input())
    if len(x) < 4 or h[0] not in x or any(i not in h for i in x):
      continue
    print("".join(x))

if __name__ == "__main__":
  main()
