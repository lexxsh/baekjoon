n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
for i in sorted(arr,key=lambda x:(x[1],x[0])):
    print(i[0],i[1])