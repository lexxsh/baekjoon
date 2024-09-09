from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
N = int(input())
output = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        output.append(str(queue.popleft() if queue else -1))
    elif command[0] == 'size':
        output.append(str(len(queue)))
    elif command[0] == 'empty':
        output.append('0' if queue else '1')
    elif command[0] == 'front':
        output.append(str(queue[0] if queue else -1))
    elif command[0] == 'back':
        output.append(str(queue[-1] if queue else -1))
print('\n'.join(output))