def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    for reserve in reserve_set:
        if reserve-1 in lost_set:
            lost_set.remove(reserve-1)
        elif reserve+1 in lost_set:
            lost_set.remove(reserve+1)
    answer = n-len(lost_set)
    return answer