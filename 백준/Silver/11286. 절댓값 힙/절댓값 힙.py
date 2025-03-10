import heapq
import sys
input = sys.stdin.readline
n = int(input())
hq = []
for i in range(n):
    num = int(input())
    if num == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq,(abs(num),num))