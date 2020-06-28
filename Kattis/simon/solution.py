for i in range(int(input())):
    s = input()
    if s[:len('simon says')] == 'simon says':
        ans = s[len('simon says'):]
        print(ans[1:])
    else:
        print("")
