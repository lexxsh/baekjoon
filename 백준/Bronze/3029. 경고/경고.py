import sys
input = sys.stdin.readline
h1,m1,s1= map(int,input().split(':'))
h2,m2,s2= map(int,input().split(':'))

if s2 < s1:
    s2 += 60
    m2 -= 1
s3 = s2-s1
if m2 < m1:
    m2 += 60
    h2 -= 1
m3 = m2-m1
h3 = (h2-h1) % 24

if h1 == h2 and m1 == m2 and s1 == s2:
    print(f"{24:02d}:{00:02d}:{00:02d}")

else:
    print(f"{h3:02d}:{m3:02d}:{s3:02d}")