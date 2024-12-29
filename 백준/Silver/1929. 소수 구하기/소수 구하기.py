def is_prime_number(n):
    sosu = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sosu[i] == True:
            for j in range(i+i,n,i):
                sosu[j] = False
                
    return [i for i in range(2,n) if sosu[i] == True]

m, n = map(int,input().split())
answer = is_prime_number(n+1)
for i in answer:
    if i >= m:
        print(i)