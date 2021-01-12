import math
from collections import Counter
smallest_mult = 1
done = False
fail = False
factors = []

for i in range(20):
    index = i
    i+=1
    factors.append([])
    
    while i % 2 == 0:
        i /= 2
        factors[index].append(2)
    for j in range(3, int(i+1), 2):
        while i % j == 0:
            i /= j
            factors[index].append(j)

max_count = {}
for i in factors:
    c = Counter(i)
    for item in c:
        try:
            if c[item] > max_count[item]:
                max_count[item] = c[item]
        except KeyError:
            max_count[item] = c[item]

for key, value in max_count.items():
    for i in range(value):
        smallest_mult *= key

print(smallest_mult)