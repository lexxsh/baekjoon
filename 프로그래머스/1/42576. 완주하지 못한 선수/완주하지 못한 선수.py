def solution(participant, completion):
    dic = {}
    answer = ''
    for part in participant:
        if not part in dic:
            dic[part] = 1
        else:
            dic[part] += 1
    for com in completion:
        dic[com] -= 1
    for key, value in dic.items():
        if not value == 0:
            answer = key
    return answer