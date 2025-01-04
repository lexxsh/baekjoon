import sys
input = sys.stdin.readline

n,m = map(int,input().split())
site = {}
for i in range(n):
    a,b = map(str,input().split())
    site[a] = b
for i in range(m):
    c = input().strip()
    print(site[c])