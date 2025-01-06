import sys
input = sys.stdin.readline

n = int(input())
s = []
dp = [0 for _ in range(n)]
for i in range(n):
    s.append(int(input()))
if n <= 2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0]+s[1]
    for i in range(2,n):
        dp[i] = max((dp[i-3]+s[i-1]),dp[i-2]) + s[i]
    print(dp[-1])