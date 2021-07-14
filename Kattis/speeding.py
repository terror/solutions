from math import floor

def main():
  ans, arr = 0, [list(map(int, input().split())) for _ in range(int(input()))]
  for i in range(len(arr)):
    a, b = arr[i]
    for j in range(i + 1, len(arr)):
      ans = max(ans, floor((arr[j][1] - b) / (arr[j][0] - a)))
  return ans

if __name__ == "__main__":
  print(main())
