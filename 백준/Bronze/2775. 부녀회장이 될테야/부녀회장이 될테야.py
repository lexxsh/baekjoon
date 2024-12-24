dp = [[0 for _ in range(15)] for _ in range(15)]
for i in range(15) :
    for j in range(15):
        if i==0:
            dp[i][j]=dp[i][j-1]+1
        else:
            dp[i][j]=dp[i][j-1]+dp[i-1][j]
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n-1])