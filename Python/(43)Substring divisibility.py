from itertools import permutations

perms = [''.join([str(y) for y in x])
         for x in permutations(range(9+1))]

sub_divisibles = []
for perm in perms:
    if (int(perm[1:4]) % 2 == 0 and int(perm[2:5]) % 3 == 0 and
            int(perm[3:6]) % 5 == 0 and int(perm[4:7]) % 7 == 0 and
            int(perm[5:8]) % 11 == 0 and int(perm[6:9]) % 13 == 0 and
            int(perm[7:10]) % 17 == 0):
        sub_divisibles.append(int(perm))

print(sum(sub_divisibles))
