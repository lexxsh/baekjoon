def solution(nums):
    cnt = len(nums)
    nums = set(nums)
    set_cnt = len(nums)
    if set_cnt <= cnt / 2:
        answer = set_cnt
    else:
        answer = cnt / 2
    return answer