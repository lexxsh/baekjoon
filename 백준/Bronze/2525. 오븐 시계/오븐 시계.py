a,b = map(int,input().split())
c = int(input())
b = b+c
while b>59:
    a+=1
    b-=60
print(a%24,b)