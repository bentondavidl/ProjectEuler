top = 4000000
n1 = 1
n2 = 1
total = 0

while n1+n2 < top:
    temp = n1 + n2
    if temp % 2 == 0:
        total += temp
    n1 = n2
    n2 = temp

print(total)