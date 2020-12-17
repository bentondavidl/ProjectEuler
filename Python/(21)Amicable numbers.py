def sum_divisors(number: int) -> int:
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors)


nums = set()
for i in range(1, 10000):
    if i == sum_divisors(num := sum_divisors(i)) and i != num:
        nums.add(i)
        nums.add(num)

print(sum(nums))
