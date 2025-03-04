import sys
input = sys.stdin.readline
t = int(input())
def leap(n):
    if t % 4 == 0:
        if t % 100 != 0 or t % 400 == 0:
            return 1
    return 0
print(leap(t))