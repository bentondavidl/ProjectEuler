import itertools

print(str(list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[
      999999]).replace('(', '').replace(', ', '').replace(')', ''))