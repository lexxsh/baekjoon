import sys
from collections import deque

n = int(input())
q = deque()
for i in range(1,n+1):
    q.append(i)
while 1:
    if len(q) == 1:
        break
    else:
        q.popleft()
        q.append(q.popleft())
print(*q)