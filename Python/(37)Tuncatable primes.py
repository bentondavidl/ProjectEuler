import math

truncatable = set()


def check_prime(number: int) -> bool:
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(number))+1, 2):
        if number % i == 0:
            return False
    return True


def check_left(number: int) -> bool:
    num_str = str(number)
    while len(num_str) > 0:
        if not check_prime(int(num_str)):
            return False
        num_str = num_str[1:]
    return True


def check_right(number: int) -> bool:
    num_str = str(number)
    while len(num_str) > 0:
        if not check_prime(int(num_str)):
            return False
        num_str = num_str[:-1]
    return True


i = 7
while len(truncatable) < 11:
    i += 2
    if check_left(i) and check_right(i):
        truncatable.add(i)

print(sum(truncatable))
