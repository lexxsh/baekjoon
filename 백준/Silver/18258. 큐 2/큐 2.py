import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(n):
    a = list(input().split())
    if a[0]=='push':
        queue.append(int(a[1]))
    elif a[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif a[0] =='front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif a[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])