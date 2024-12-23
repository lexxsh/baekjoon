x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
ans1,ans2=0,0
if x1 == x2:
    ans1 = x3
elif x2 == x3:
    ans1 = x1
else:
    ans1 = x2
if y1 == y2:
    ans2 = y3
elif y2 == y3:
    ans2 = y1
else:
    ans2 = y2
print(ans1,ans2)