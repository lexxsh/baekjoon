a,b,c = map(int,input().split())
money = [0] * 100
ans = 0
for i in range(3):
    start,end = map(int,input().split())
    for j in range(start,end):
        money[j]+=1
for i in money:
    if i == 1:
        ans += i*a
    elif i ==2:
        ans += i*b
    else:
        ans += i*c
print(ans)