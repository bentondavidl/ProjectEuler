def wheel(n):
    factors = set()
    ws = [1,2,2,4,2,4,2,4,6,2,6]
    f = 2
    w = 0

    while f * f <= n:
        if n % f == 0:
            factors.add(f)
            n /= f
        else:
            f += ws[w]
            w = 3 if w == 10 else (w + 1)
    factors.add(n)
    
    return factors

i = 644
count = 0
c_start = 0
target = 4
while True:
    if len(factors := wheel(i)) == target:
        # print(i, factors)
        if count == 0:
            c_start = i
        count += 1
    else:
        count = 0
    if count == target:
        break
    i += 1

print(c_start)
