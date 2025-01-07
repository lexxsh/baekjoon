import sys
input = sys.stdin.readline
n = int(input())
a = input().strip()
stack = []
num = []
for i in range(n):
    num.append(int(input()))
for i in a:
    if 'A' <= i <= 'Z':
        stack.append(num[ord(i)-ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if i == '*':
            stack.append(num1 * num2)
        if i == '+':
            stack.append(num1 + num2)
        if i == '/':
            stack.append(num1 / num2)
        if i == '-':
            stack.append(num1 - num2)
print(format(*stack,".2f"))            