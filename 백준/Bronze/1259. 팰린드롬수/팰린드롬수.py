ans = 2
while 1:
    lst = []
    a = input()
    if a =='0':
        break
    for i in a:
        lst.append(i)
    for i in range(len(lst)):
        if(lst[i] != lst[len(lst)-i-1]):
            ans = 0
            break
        else:
            ans = 1
    if ans == 1:
        print('yes')
    else : 
        print('no')