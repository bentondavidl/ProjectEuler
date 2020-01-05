import math

target = 600851475143
max_prime = 0

while target % 2 == 0:
    target /= 2
for i in range(3, math.floor(math.sqrt(target)), 2):
    while target % i == 0:
        target /= i
        if i > max_prime:
            max_prime = i

print(max_prime)


