def solution(numbers):
    sum = 0
    for i in range(1,10):
        if not i in numbers:
            sum += i
    return sum