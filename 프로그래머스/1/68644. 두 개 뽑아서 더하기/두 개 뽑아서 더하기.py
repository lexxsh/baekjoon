def solution(numbers):
    answer = []
    k = len(numbers)
    for i in range(k):
        for j in range(i+1,k):
            answer.append(numbers[i]+numbers[j])
            print(i,j)
    answer = sorted(set(answer))
    print(answer)
    return answer