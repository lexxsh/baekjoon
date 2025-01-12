import sys
from collections import defaultdict, deque
def DFS(graph, start):
    visit = list()
    stack = list()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))
    print(*visit,sep=" ")
    return visit
    
def BFS_list(graph,start):
    visit = list()
    queue = list()
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    print(*visit,sep=" ")
    return visit

def BFS_deque(graph,start):
    visit = set()
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.add(node)
            queue.extend(graph[node])
    print(*visit,sep=" ")
    return visit

def BFS_deque_2(graph,start):
    visit = [False] * (n + 1)
    queue = deque()
    queue.append(start)
    ans = list()
    while queue:
        node = queue.popleft()
        if not visit[node]:
            visit[node] = True
            ans.append(node)
            queue.extend(graph[node])
    print(*ans,sep=" ")
    return visit

input = sys.stdin.readline
n,m,v = map(int,input().split())

G = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
for key in G:
    G[key].sort()
DFS(G,v)
# BFS_list(G,v)
# BFS_deque(G,v)
BFS_deque_2(G,v)