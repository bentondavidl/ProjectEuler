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

target = 1000000
primes = [2]
current_number = 1

while primes[-1] < target/10:
    current_number += 1
    flag = True
    for prime in primes:
        if flag and current_number % prime == 0:
            flag = False
            break
    primes.append(current_number) if flag else None

best = 0
b_len = 0
for dist in range(len(primes)-1):
    for start in range(len(primes)-dist):
        tot = sum(primes[start:start+dist])
        if tot > target: break
        if check_prime(tot): 
            best = tot
            b_len = dist

print(best, b_len)
