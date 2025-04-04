def get_yaksu(num):
    cnt = 0
    for i in range(1,int(num ** (1/2))+1):
        if num % i == 0:
            cnt += 1
            if i < num // i:
                cnt += 1
    return cnt
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if get_yaksu(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
    