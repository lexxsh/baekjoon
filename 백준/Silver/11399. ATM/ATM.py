import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
time = 0
p.sort()
for i in range(n):
    time += sum(p[0:i+1])
print(time)