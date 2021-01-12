from itertools import permutations

nums = '123456789'
perms = permutations(nums)

pandigital = set()

for perm in perms:
    for i in range(1, 8):
        for j in range(i, 9):
            try:
                if int(''.join(perm[:i])) * int(''.join(perm[i:j])) == int(''.join(perm[j:])):
                    pandigital.add(int(''.join(perm[j:])))
            except ValueError:
                pass

print(sum(list(pandigital)))
