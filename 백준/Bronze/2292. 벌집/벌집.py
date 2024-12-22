n = int(input())
j,k,cnt = 6,1,1
while k<n:
    k+=j
    j+=6
    cnt+=1
print(cnt)