n,m = map(int,input().split())
dp = [list(map(int,input())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i>0 and j>0 and dp[i][j]!=0:
            dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
            
print(max(max(row) for row in dp)**2)