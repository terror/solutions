def main():
    print(26-lis(input()))

def lis(arr):
    lis = [1]*len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j]+1: lis[i] = lis[j]+1
    return max(lis)

main()
