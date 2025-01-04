import sys
input = sys.stdin.readline

n,m = map(int,input().split())
heard = set()
see = set()
for i in range(n):
    heard.add(input().strip())
for i in range(m):
    see.add(input().strip())
answer = heard & see
print(len(answer))
print(*sorted(answer),sep="\n")