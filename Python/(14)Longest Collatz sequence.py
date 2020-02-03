n = 0
max_count = 0
best_start = 0

for n1 in range(100000,1000000):
    n = n1
    count = 0
    while(n > 1):
        if(n % 2 == 0):
            n /= 2
        else:
            n = 3*n + 1
        count += 1

    if (count > max_count):
        max_count = count
        best_start = max(best_start, n1)

print(best_start)
