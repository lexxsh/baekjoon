a = input().strip()
b = input().strip()

if len(a) < len(b):
    a, b = b, a 
max_length = 0

row = [0] * (len(a) + 1)
for i in range(1, len(b) + 1):
    prev = 0
    for j in range(1, len(a) + 1):
        temp = row[j]
        if b[i-1] == a[j-1]:
            row[j] = prev + 1
            max_length = max(max_length, row[j])
        else:
            row[j] = 0
        prev = temp

print(max_length)