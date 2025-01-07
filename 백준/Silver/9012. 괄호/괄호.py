import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    stack = []
    a = input().strip()
    for i in a:
        if i == '(':
            stack.append(i)
        elif i ==')' and stack:
            stack.pop()
        else:
            stack.append(i)
            break
    if stack:
        print('NO')
    else:
        print('YES')
                