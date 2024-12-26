a = list(input() for _ in range(3))
ans = 0
for idx, i in enumerate(a):
    if i[0] == 'F' or i[0] == 'B':
        continue
    else:
        ans = int(i) + (3-idx)
if ans % 3 == 0 and ans % 5 == 0:
    print("FizzBuzz")
elif ans % 3 == 0 and ans % 5 != 0:
    print("Fizz")
elif ans % 3 != 0 and ans % 5 == 0:
    print("Buzz")
elif ans % 3 != 0 and ans % 5 != 0:
    print(ans)