for i in range(int(input())):
    s = input()
    if s[:len('Simon says')] == 'Simon says':
        print(s[len('Simon says'):])
