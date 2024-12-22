t = int(input())
ans = []
for i in range(t):
    a,b = input().split()
    a = int(a)
    for j in b:
        for k in range(a):
            ans.append(j)
    for j in ans:
        print(j, end='')
    print()
    ans = []