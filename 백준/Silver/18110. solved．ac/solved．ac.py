import sys
input = sys.stdin.readline
def round_up_half(number):
    import math
    return math.floor(number+0.5)
n = int(input())
a = list(int(input()) for _ in range(n))
a.sort()
avg = round_up_half(n * (15/100))
sum = 0
for i in range(avg,n-avg):
    sum += a[i]
if sum == 0:
    print(0)
else: 
    print(round_up_half(sum / (n-2*avg))) 