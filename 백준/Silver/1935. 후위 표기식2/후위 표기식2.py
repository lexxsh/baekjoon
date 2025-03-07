n = int(input())
s = input()
num = []
for i in range(n):
    num.append(int(input()))
stack = []
for a in s:
    if 'A' <= a <= 'Z':
        stack.append(num[ord(a)-ord('A')])
    else:
        t1 = stack.pop()
        t2 = stack.pop()
        if a == '+':
            stack.append(t2+t1)
        elif a == '-':
            stack.append(t2-t1)
        elif a == '*':
            stack.append(t2*t1)
        elif a == '/':
            stack.append(t2/t1)
print(f'{stack[-1]:.2f}')