import sys
input = sys.stdin.readline
n = int(input())
word = set([])
for i in range(n):
    t = input().strip()
    word.add(t)
ans = sorted(word, key = lambda x:(len(x),x))
print(*ans,sep='\n')