k,n = map(int,input().split())
a=[]
for i in range(k):
    a.append(int(input()))
start,end = 1,max(a)
ans = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in a:
        cnt += i//mid
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1
        ans = mid
print(ans)