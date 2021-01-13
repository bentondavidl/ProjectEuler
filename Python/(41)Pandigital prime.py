import math
from itertools import permutations


def check_prime(number: int) -> bool:
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(number))+1, 2):
        if number % i == 0:
            return False
    return True


perms = [1]

for i in range(2, 10):
    perms.extend([int(''.join([str(y) for y in x]))
                  for x in permutations(range(1, i+1))])

for perm in sorted(perms, reverse=True):
    if check_prime(perm):
        print(perm)
        break
