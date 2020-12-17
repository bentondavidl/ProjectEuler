n1 = 1
n2 = 1
total = 0
i = 2

while len(str(n2)) < 1000:
    temp = n1 + n2
    if temp % 2 == 0:
        total += temp
    n1 = n2
    n2 = temp
    i += 1

print(i)
