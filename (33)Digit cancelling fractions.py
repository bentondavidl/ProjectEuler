fractions = []

for num in range(10, 100):
    for den in range(num+1, 100):
        try:
            if num % 10 == den % 10 and num/den == (num // 10)/(den // 10):
                fractions.append((num, den))
            if num % 10 == den // 10 and num/den == (num // 10)/(den % 10):
                fractions.append((num, den))
            if num // 10 == den % 10 and num/den == (num % 10)/(den // 10):
                fractions.append((num, den))
            if num // 10 == den // 10 and num/den == (num % 10)/(den % 10):
                fractions.append((num, den))
        except ZeroDivisionError:
            pass

fractions = [x for x in fractions if x[0] % 10 != 0 and x[1] % 10 != 0]

prod = [1, 1]
for num, den in fractions:
    prod[0] *= num
    prod[1] *= den

print(prod[0]/prod[1])
