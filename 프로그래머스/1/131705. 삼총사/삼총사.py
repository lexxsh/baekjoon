from itertools import combinations
def solution(number):
    answer = 0
    com = list(combinations(number,3))
    for num in com:
        if sum(num) == 0:
            answer += 1
    return answer