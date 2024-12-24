import math
t = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())
cnt1 = 0
for i in a:
    cnt1 += math.ceil(i/b)
print(cnt1)
print(t//c,t%c)