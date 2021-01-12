max_val = 1000
best_n = 0
best_ab = (0, 0)
primes = [2]


def check_prime(number: int) -> bool:
    if number < 2:
        return False
    for prime in primes:
        if number % prime == 0:
            return False
    primes.append(number)
    return True


for a in range(-1*max_val, max_val):
    for b in range(-1*max_val, max_val+1):
        n = 0
        while True:
            if (n*n + a*n + b) in primes or check_prime(n*n + a*n + b):
                n += 1
                continue
            break
        if n > best_n:
            best_n = n
            best_ab = (a, b)

print(best_ab[0]*best_ab[1])
