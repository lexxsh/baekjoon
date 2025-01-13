m = int(input())
n = int(input())
end = int(n**(1/2))
ans = [False,False] + [True] *(n+1)
prime = []
sum = 0
min = n
for i in range(2,n+1):
    if ans[i]:
        prime.append(i)
        for j in range(2*i,n+1,i):
            ans[j]=False
for i in prime:
    if i >= m :
       sum += i
       if min>i:
           min = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)