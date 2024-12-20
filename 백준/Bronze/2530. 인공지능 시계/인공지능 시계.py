a,b,c = map(int,input().split())
d = int(input())
c = c+d
while c>59:
    b+=1
    c-=60
while b>59:
    a+=1
    b-=60
print(a%24,b,c)