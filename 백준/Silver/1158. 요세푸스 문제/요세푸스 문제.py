n,k=map(int,input().split())
l=list(range(1,n+1))
j=0
print('<'+', '.join(str(l.pop(j:=(j+k-1)%len(l)))for _ in'_'*n)+'>')