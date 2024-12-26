import sys
n = int(input())
cnt = 0
for i in range(sys.maxsize):
    if '666' in str(i):
        cnt += 1
        if n == cnt:
            print(i)
            break