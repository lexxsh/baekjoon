t = int(input())
a = input()
cnt = 0
for idx, i in enumerate(a):
    cnt += (ord(i)-96)*(31**idx)
print(cnt)