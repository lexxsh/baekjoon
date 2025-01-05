import sys
input = sys.stdin.readline

dp = [0,0]
n = int(input())
for i in range(2,1000001):
    if i % 6 == 0:
        dp.append(min(dp[i//3],dp[i//2],dp[i-1])+1)
    elif i % 3 == 0:
        dp.append(min(dp[i//3],dp[i-1])+1)
    elif i % 2 == 0:
        dp.append(min(dp[i//2],dp[i-1])+1)
    else:
        dp.append(dp[i-1]+1)
print(dp[n])