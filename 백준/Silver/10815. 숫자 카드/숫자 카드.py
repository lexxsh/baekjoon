import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int,input().split()))
ans = []
def binary_search(t,arr,start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if arr[mid] == t:
        return 1
    elif arr[mid] > t:
        return binary_search(t,arr,start,mid-1)
    else:
        return binary_search(t,arr,mid+1,end)
for i in arr2:
    ans.append(binary_search(i,arr,0,len(arr)-1))
print(*ans, sep=' ')