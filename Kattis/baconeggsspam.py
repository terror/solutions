names = {}
orders = []

while True:
    n = int(input())
    names.clear()
    orders.clear()
    if n == 0:
        break
    for i in range(n):
        line = input().split()
        names[line[0]] = []
        for j in range(1, len(line)):
            names[line[0]].append(line[j])
            orders.append(line[j])
    orders.sort()
    if(len(orders) != len(set(orders))):
        orders = list(dict.fromkeys(orders))
    for i in range(len(orders)):
        l = [k for k, v in names.items() if orders[i] in v]
        l.sort()
        res = str(l)[1:-1]
        res = res.replace(',', "").replace("'", "")
        print("{0} {1}".format(orders[i], res))
    print("\n")
