def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        num = ''
        for j in range(i,i+len(p)):
            num += t[j]
        if int(num) <= int(p):
            answer += 1
    return answer