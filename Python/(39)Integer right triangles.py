max_solutions = (0, 0)

for i in range(1, 1000):
    count = 0
    for c in range(1, i+1):
        for b in range(1, i-c+1):
            a = i-b-c
            if a < b < c and a*a + b*b == c*c:
                count += 1
    if count > max_solutions[1]:
        max_solutions = (i, count)

print(max_solutions)
