t = int(input())
n = list(map(int,input().split()))
sum = 0
for i in n:
    sum += i/max(n)*100
print(sum/t)