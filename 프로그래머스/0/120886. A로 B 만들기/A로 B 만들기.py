def solution(before, after):
    dic= {}
    for char in before:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    for char in after:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    for key,value in dic.items():
        if not value % 2 == 0:
            return 0
    return 1