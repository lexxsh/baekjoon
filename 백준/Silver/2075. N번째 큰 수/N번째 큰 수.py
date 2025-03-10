import heapq
n = int(input())
hq= []
for i in range(n):
    num = list(map(int,input().split()))
    if i == 0:
        for n in num:
            heapq.heappush(hq,n)
    else:
        for n in num:
            if n > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq,n)
print(heapq.heappop(hq))