n1 = input()
n2 = input()

# make them both same len
if len(n1) > len(n2):
  n2 = '0' * (len(n1) - len(n2)) + n2
else:
  n1 = '0' * (len(n2) - len(n1)) + n1

new_num1 = ''
new_num2 = ''

for i in range(len(n1)):
  if i >= len(n2):
    break
  if n1[i] < n2[i]:
    new_num2 += n2[i]
  elif n1[i] > n2[i]:
    new_num1 += n1[i]
  else: # append both cuz same either way
    new_num1 += n1[i]
    new_num2 += n2[i]

# check if all nums got replaced or not
if len(new_num1):
  print(int(new_num1))
else:
  print("YODA")

if len(new_num2):
  print(int(new_num2))
else:
  print("YODA")
