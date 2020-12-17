def is_abundant(number: int) -> bool:
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors) > number


abundants = [x for x in range(28123) if is_abundant(x)]

print(abundants[-5:])

all_sums = set()
for i in abundants:
    for j in abundants:
        all_sums.add(i+j)

all_sums = list(all_sums)

print(all_sums[-5:])

non_abundants = [x for x in range(28123) if x not in all_sums]

print(sum(non_abundants))
