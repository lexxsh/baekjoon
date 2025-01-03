from collections import Counter
import sys
import math
input = sys.stdin.readline
def cnt(data):
    dict = Counter(data)
    max_freq = max(dict.values())
    modes = [num for num,freq in dict.items() if freq == max_freq]

    if len(modes) >= 2:
        return sorted(modes)[1]
    else:
        return sorted(modes)[0]    
    
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
print(math.floor(sum(a)/len(a)+0.5))
print(a[int(len(a)/2)])
print(cnt(a))
print(a[len(a)-1]-a[0])