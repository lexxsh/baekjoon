import sys
from collections import defaultdict
input = sys.stdin.readline

def dfs(g,start):
    visit=list()
    stack=list()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(g[node]))
    print(len(visit)-1)
    return visit

G=defaultdict(list)
t = int(input())
n = int(input())
for i in range(n):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dfs(G,1)