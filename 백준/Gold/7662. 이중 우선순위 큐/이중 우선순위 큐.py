import sys,heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    min_heap = []
    max_heap = []
    check = {}
    k = int(input())
    
    for _ in range(k):
        a, b = map(str, input().split())
        if a == 'I':
            heapq.heappush(min_heap, int(b))
            heapq.heappush(max_heap, (-int(b), int(b)))
            if b in check:
                check[b] += 1
            else:
                check[b] = 1
        elif a == 'D':
            if b == '1':
                while max_heap and check[str(max_heap[0][1])] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = heapq.heappop(max_heap)[1]
                    check[str(max_val)] -= 1
            elif b == '-1':
                while min_heap and check[str(min_heap[0])] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    check[str(min_val)] -= 1
    while min_heap and check[str(min_heap[0])] == 0:
        heapq.heappop(min_heap)
    while max_heap and check[str(max_heap[0][1])] == 0:
        heapq.heappop(max_heap)
        
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(f"{max_heap[0][1]} {min_heap[0]}")