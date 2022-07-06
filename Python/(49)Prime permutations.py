import math

def check_prime(number: int) -> bool:
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(number))+1, 2):
        if number % i == 0:
            return False
    return True

n = 1488

while n + 6660 < 10000:
    nums = []
    for i in range(3):
        val = n + 3330*i
        if not check_prime(val):
            break
        nums.append(val)

    if len(nums) == 3 and len(set(''.join(sorted(str(x))) for x in nums)) == 1:
        break
    n += 1

print(''.join(str(x) for x in nums))