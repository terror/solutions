def main():
  n = int(input())
  if n & 1:
    print("Bob")
    exit()
  print("Alice")
  print(1)

if __name__ == '__main__':
  main()
