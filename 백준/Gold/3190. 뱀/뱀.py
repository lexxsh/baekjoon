from collections import deque

def check_direction(now, turn):
    if now == 'E' and turn == 'D':
        return 'S'
    elif now == 'E' and turn == 'L':
        return 'N'
    elif now == 'N' and turn == 'D':
        return 'E'
    elif now == 'N' and turn == 'L':
        return 'W'
    elif now == 'W' and turn == 'D':
        return 'N'
    elif now == 'W' and turn == 'L':
        return 'S'
    elif now == 'S' and turn == 'D':
        return 'W'
    elif now == 'S' and turn == 'L':
        return 'E'
    
n = int(input())
k = int(input())

apple = []
for i in range(k):
    a,b = map(int, input().split())
    apple.append((a,b))

l = int(input())

turn = {}
for i in range(l):
    a,b = map(str, input().split())
    turn[int(a)] = b
cnt = 0
snake = deque([(1,1),])
direction = 'E'
    
while 1:
    cnt += 1
    if direction == 'E':
        new = (snake[-1][0],snake[-1][1] + 1)
    elif direction == 'N':
        new = (snake[-1][0]-1,snake[-1][1])
    elif direction == 'S':
        new = (snake[-1][0]+1,snake[-1][1])
    elif direction == 'W':
        new = (snake[-1][0],snake[-1][1] - 1)
    if new in snake or new[0] in [0,n+1] or new[1] in [0,n+1]:
        break
    else:
        snake.append(new)
        if new in apple:
            apple.remove(new)
        else:
            snake.popleft()
        if cnt in turn:
            direction = check_direction(direction, turn[cnt])

print(cnt)