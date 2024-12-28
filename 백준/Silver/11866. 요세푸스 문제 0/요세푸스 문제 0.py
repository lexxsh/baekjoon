import sys
input = sys.stdin.readline

n,k = map(int,input().split())
list = list(range(1,n+1))
idx = 0
result = []
while list:
    idx = (idx + k - 1) % len(list)
    result.append(list.pop(idx))
print("<", end="")
for i in range(n-1):
    print(result[i], end=", ")
print(f"{result[n-1]}>")