import sys
input = sys.stdin.readline
dp = [1,1,1]
for i in range(3,100):
    dp.append(dp[i-2]+dp[i-3])
for _ in range(int(input())):
    n = int(input())
    print(dp[n-1])