def main():
  *problems, n = list(map(int, input().split()))
  (lambda x, y: print("YES") if n >= 3 and 0 not in problems and n <= sum(problems) else print("NO"))(problems, n)

main()
