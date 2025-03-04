import sys
input = sys.stdin.readline
a,b,c,m = map(int,input().split())
hour = 24
tire = 0
job = 0
while(hour):
    hour -= 1
    if tire+a > m:
        tire = max(0,tire - c)
    else:
        tire += a
        job += b
print(job)
