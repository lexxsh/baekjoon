n = int(input())
ans = [1,1]
for i in range(2,90):
    ans.append(ans[i-1] + ans[i-2])

print(ans[n-1])