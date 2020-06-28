for i in range(int(input())):
    line = input()
    if line == 'P=NP':
        print('skipped')
    else:
        line = line.split('+')
        print(int(line[0]) + int(line[1]))
