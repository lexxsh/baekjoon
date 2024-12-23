n = int(input())
a = list(map(int,input().split()))
cnt = n
for i in a:
    if i == 1:
        cnt -=1
    for j in range(2,i):
        if i%j == 0:
            cnt-=1
            break
print(cnt)