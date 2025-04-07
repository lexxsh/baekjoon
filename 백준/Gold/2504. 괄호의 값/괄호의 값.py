s = input()
stack = []
r = 1
ans = 0
for i in range(len(s)):
    if s[i] == '(':
        r *= 2
        stack.append('(')
    elif s[i] == '[':
        r *= 3
        stack.append('[')
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        elif s[i-1] == '(':
            ans += r
        stack.pop()
        r //= 2
    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        elif s[i-1] == '[':
            ans += r
        stack.pop()
        r //= 3
if stack:
    print(0)
else:
    print(ans)
