import sys
def input(): return sys.stdin.readline().rstrip()
left_stack = list(input())
right_stack = []
m = int(input())
for i in range(m):
    t = list(map(str,input().split()))
    if left_stack and t[0] == 'L':
        right_stack.append(left_stack.pop())
    elif right_stack and t[0] == 'D':
        left_stack.append(right_stack.pop())
    elif left_stack and t[0] == 'B':
        left_stack.pop()
    elif t[0] == 'P':
        left_stack.append(t[1])
right_stack.reverse()
print(''.join(left_stack+right_stack))