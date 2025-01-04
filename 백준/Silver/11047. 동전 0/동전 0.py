import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
ans = 0
for i in range(n):
    coin.insert(0,int(input().strip()))
for i in coin:
    ans += k//i
    k %= i
print(ans)