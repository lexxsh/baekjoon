def manhetten(x1,y1,x2,y2):
    return abs(x2-x1) + abs(y2-y1)

def find_arr(arr,n):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == n:
                return i,j
            
def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'
    arr = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = number
        elif number in [3,6,9]:
            answer += 'R'
            right = number
        else:
            x1,y1 = find_arr(arr,number)
            x_l,y_l = find_arr(arr,left)
            x_r,y_r = find_arr(arr,right)
            if manhetten(x1,y1,x_l,y_l) > manhetten(x1,y1,x_r,y_r):
                answer += 'R'
                right = number
            elif manhetten(x1,y1,x_l,y_l) < manhetten(x1,y1,x_r,y_r):
                answer += 'L'
                left = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
    return answer