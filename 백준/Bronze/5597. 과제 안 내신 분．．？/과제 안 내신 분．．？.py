arr = [False]*30
for i in range(28):
    n = int(input())
    arr[n-1] = True
for i in range(len(arr)):
    if not arr[i]:
        print(i+1)