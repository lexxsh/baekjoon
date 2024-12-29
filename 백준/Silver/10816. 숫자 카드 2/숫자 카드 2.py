import sys
input = sys.stdin.readline
ans = [0] * (20000001)
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
for i in a:
    ans[i+10000000] += 1
for i in b:
    print(ans[i+10000000],end=" ")