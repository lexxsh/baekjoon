import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dogam = {}
dogam2 = {}
for i in range(n):
    name = input().strip()
    dogam[i+1] = name
    dogam2[name] = i+1
for i in range(m):
    question = input().strip()
    if question.isdecimal():
        print(dogam[int(question)])
    else:
        print(dogam2[question])