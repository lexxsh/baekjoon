s = input()
stack = []
t = 0
def printstack(stack):
    while stack:
        print(stack.pop(),end='')
for a in s:
    if a == '<':
        t = 1
        printstack(stack)
        print('<', end='')
    elif a == '>':
        t = 0
        print('>', end='')
    elif a == ' ':
        printstack(stack)
        print(' ',end='')
    else:
        if t == 0:
            stack.append(a)
        else:
            print(a,end='')
printstack(stack)