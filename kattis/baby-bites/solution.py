def check(n, s):
    for i in range(n):
        # if s[i] is not consistent w/ i+1
        if(s[i] != "mumble" and int(s[i]) != i+1):
            return False
    return True


n = int(input())
s = input().split()

if(check(n, s)):
    print("makes sense")
else:
    print("something is fishy")
