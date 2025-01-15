import sys
from math import lcm
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a,b= map(int,input().split())
    print(lcm(a,b))
        