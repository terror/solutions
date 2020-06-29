n = int(input())

for i in range(n):
    c = False
    k = int(input())
    name = input()
    items = [input() for _ in range(k)]
    if 'pea soup' in items and 'pancakes' in items:
        print(name)
        c = True
        break
if not c:
    print('Anywhere is fine I guess')
