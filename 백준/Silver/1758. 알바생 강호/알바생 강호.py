import sys
input = sys.stdin.readline
n = int(input())
tip = []
ans = 0
for i in range(n):
    tip.append(int(input()))
tip = sorted(tip,reverse = True)
for i in range(len(tip)):
    ans += max(tip[i] - (i), 0)
print(ans)