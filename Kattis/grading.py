import string

A = list(map(lambda x: x.upper(), string.ascii_lowercase))

def main(grades, curr):
  for k, v in grades.items():
    if curr >= v:
      print(k)
      return
  print('F')

if __name__ == '__main__':
  main({ A[index]: grade for index, grade in enumerate(list(map(int, input().split()))) }, int(input()))
