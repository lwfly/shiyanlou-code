a = 1
b = 0
c = 0
for a in range(1,101):
    b = a // 10
    c = a % 10
    if a % 7 == 0 or b == 7 or c == 7:
        continue
    print(a)

