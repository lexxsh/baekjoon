import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs(graph,start):
    visit = [0] * (n+1)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if visit[node] == 0:
            visit[node] = node
            queue.extend(graph[node])
    return visit
def bfs_2(graph,start):
    visit = [0] * (n+1)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if visit[adj] == 0:
                visit[adj] = node
                queue.append(adj)
    return visit
n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
ans = bfs_2(tree,1)
print(*ans[2:],sep="\n")