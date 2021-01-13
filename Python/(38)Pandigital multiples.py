from itertools import permutations

pan = permutations('123456789')
pan = [int(''.join(x)) for x in pan]


def check_pandigital(num):
    num_int = int(num)

    if len(str(num)) != 9:
        return False

    if any([num_int == x for x in pan]):
        return True
    return False


def get_concat(num):
    total = ''
    i = 0
    while len(total) < 9:
        i += 1
        total += str(num*i)
    return int(total)


max_pandigital = 0
i = 0
while i < 999999:
    i += 1
    temp = get_concat(i)
    if check_pandigital(temp):
        print('found', temp)
        max_pandigital = max(max_pandigital, temp)

print(max_pandigital)
