import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = a+b
ans = sorted(c)
print(*ans,sep = ' ')