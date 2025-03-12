def solution(s):
    arr = s.split(' ')
    answer = ''
    for idx,word in enumerate(arr):
        if not idx == 0:
            answer += ' '
        for idx,a in enumerate(word):
            if idx % 2 == 0:
                answer += a.upper()
            else:
                answer += a.lower()
    return answer