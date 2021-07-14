def main():
  n = int(input())

  for i in range(n):
    name, yearS, yearB, courses = list(map(str, input().split()))
    status = check_status(yearS, yearB, courses)
    print(name, status)

def check_status(yearS, yearB, courses):
  yearS = yearS.split('/')
  yearB = yearB.split('/')
  if int(yearS[0]) >= 2010:
    return 'eligible'
  elif int(yearB[0]) >= 1991:
    return 'eligible'
  elif int(courses) >= 41:
    return 'ineligible'
  else:
    return 'coach petitions'

main()
