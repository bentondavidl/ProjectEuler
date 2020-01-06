import math
target = 10
primes = [2]
current_number = 2

while True:
    current_number += 1
    flag = True
    for prime in primes:
        if prime > math.sqrt(current_number): break
        if current_number % prime == 0:
            flag = False
        if not flag: break
    primes.append(current_number) if flag else None
    if primes[-1] >= target:
        del primes[-1]
        break

print(sum(primes))