import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range(n):
    a = list(map(int,input().split()))
    answer = sorted(a+answer,reverse=True)[:n]
print(answer[-1])