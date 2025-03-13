def solution(s):
    dic = {'p': 0,'y':0}
    for char in s:
        if char == 'p' or char == 'P':
            dic['p'] += 1
        elif char == 'y' or char =='Y':
            dic['y'] += 1
    if dic['p'] == dic['y']:
        return True
    else:
        return False