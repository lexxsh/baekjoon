s = input()
stack = []
ans = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')' and s[i-1] == '(':
        stack.pop()
        ans += len(stack)
    else:
        stack.pop()
        ans += 1
print(ans)