target = 10001
primes = []
current_number = 1

while len(primes) < target:
    current_number += 1
    flag = True
    for prime in primes:
        if flag and current_number % prime == 0:
            flag = False
            break
    primes.append(current_number) if flag else None

print(primes[-1])
