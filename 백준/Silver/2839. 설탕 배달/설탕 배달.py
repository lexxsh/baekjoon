n = int(input())
dp = list(-1 for _ in range(5001))
dp[3],dp[5] = 1,1
for i in range(6,n+1):
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-3], dp[i-5]) +1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
print(dp[n])