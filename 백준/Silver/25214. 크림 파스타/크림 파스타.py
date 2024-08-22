n = int(input())
a = list(map(int,input().split()))

d = [0]*n
min_value = a[0]
for i in range(1,n):
    min_value = min(min_value,a[i])
    d[i] = max(d[i-1],a[i]-min_value)

print(*d)