def solution(x):
    a = 0
    for num in str(x):
        a += int(num)
    if x % a == 0:
        return True
    else:
        return False