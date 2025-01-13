n = int(input())
num = n
cycle = 0
while 1:
    num = (num%10)*10 + ((num//10 + num%10)%10)
    cycle+=1
    if n == num:
        break
print(cycle)