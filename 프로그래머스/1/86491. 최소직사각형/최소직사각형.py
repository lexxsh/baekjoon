def solution(sizes):
    a = []
    b = []
    for nums in sizes:
        a.append(max(nums))
        b.append(min(nums))
    return max(a) * max(b)