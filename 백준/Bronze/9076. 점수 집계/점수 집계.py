t = int(input())
for i in range(t):
    n = list(map(int,input().split()))
    n.sort()
    if(n[3]-n[1]>3):
        print('KIN')
    else:
        print(n[1]+n[2]+n[3])