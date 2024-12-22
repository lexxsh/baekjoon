t = int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if c%a == 0:
        ans = (a * 100) + (int(c/a))
    else:
        ans = (c%a * 100) + (int(c/a) + 1)
    print(ans)