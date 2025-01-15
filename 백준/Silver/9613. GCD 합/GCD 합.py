import sys
from math import gcd
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    num = list(map(int,input().split()))
    sum = 0
    for i in range(1,num[0]+1):
        for j in range(i+1,num[0]+1):
            sum += gcd(num[i],num[j])
    print(sum)