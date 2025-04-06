import heapq
def solution(k, score):
    answer = []
    heap = []
    for num in score:
        if len(heap) < k:
            heapq.heappush(heap, num)
            answer.append(heap[0])
        else:
            heapq.heappush(heap, num)
            heapq.heappop(heap)
            answer.append(heap[0])
    return answer