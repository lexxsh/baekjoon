def solution(d, budget):
    answer = 0
    a = 0
    d = sorted(d)
    for i in range(len(d)):
        if not a+d[i] > budget:
            a += d[i]
            answer += 1
        else:
            return answer
    return answer