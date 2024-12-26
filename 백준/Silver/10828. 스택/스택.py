import sys
n = int(input())
arr = []
for i in range(n):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push':
        arr.append(int(a[1]))
    elif a[0] == 'pop':
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    elif a[0] == 'size':
        print(len(arr))
    elif a[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif a[0] == 'top':
        if not arr:
            print(-1)
        else:
            print(arr[-1])
        