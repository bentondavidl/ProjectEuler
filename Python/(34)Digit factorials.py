import math
MAX_POSSIBLE_VAL = 2540160  # == 9! * 7

total = 0
for i in range(3, MAX_POSSIBLE_VAL):
    i_str = str(i)
    if sum([math.factorial(int(x)) for x in i_str]) == i:
        total += i

print(total)
