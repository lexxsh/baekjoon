from collections import deque
n = int(input())
q = deque()
for i in range(2,n+1):
    q.append(i)
a = list(map(int,input().split()))
ballon = 1
print(ballon,end=" ")
while q:
    if a[ballon-1] > 0:
        for i in range(1,a[ballon-1]):
            q.append(q.popleft())
        ballon=q.popleft()
    else:
        for i in range(1,abs(a[ballon-1])):
            q.appendleft(q.pop())
        ballon=q.pop()
    print(ballon,end=" ")    