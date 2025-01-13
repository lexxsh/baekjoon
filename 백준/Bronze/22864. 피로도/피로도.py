a,b,c,m = map(int,input().split())
work = 0
tire = 0

for i in range(24):
    if tire + a <= m:
           work += b
           tire += a
    else:
        if tire - c >= 0:
            tire -= c
        else:
            tire = 0
print(work)