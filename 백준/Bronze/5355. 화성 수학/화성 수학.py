t = int(input())
for i in range(t):
    text = input().split()
    a = float(text.pop(0))
    for j in text:
        if j == '@':
            a *= 3
        elif j == '%':
            a += 5
        elif j == '#':
            a -= 7
    print(format(a,".2f"))