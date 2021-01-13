import math
primes = []


def check_prime(number: int) -> bool:
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(number)), 2):
        if number % i == 0:
            return False
    return True


def rotations(num):
    num_str = str(num)
    rots = []
    for i in range(len(num_str)):
        num_str = num_str[1:]+num_str[:1]
        rots.append(int(num_str))
    return rots


checked = set()
circular_primes = set()
for i in range(1000000):
    if i in checked:
        continue
    rots = rotations(i)
    checked.update(rots)
    test = map(check_prime, rots)
    if all(test):
        circular_primes.update(rots)
        print('found ', rots)

# primes = []
# circular_primes = [x for x in circular_primes if check_prime(x)]

print(len(list(circular_primes)))
