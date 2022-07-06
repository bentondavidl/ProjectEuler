from collections import defaultdict

def wheel(n):
    factors = defaultdict(lambda: 0)
    ws = [1,2,2,4,2,4,2,4,6,2,6]
    f = 2
    w = 0

    while f * f <= n:
        if n % f == 0:
            factors[f] += 1
            n /= f
        else:
            f += ws[w]
            w = 3 if w == 10 else (w + 1)
    factors[n] += 1
    
    return dict(factors)

def totient(n):
    if n == 1:
        return 1
    totient = 1
    for k,v in wheel(n).items():
        totient *= k ** (v-1) * (k - 1)
    return totient

def find_last_n_digits(base, exp, n):
    tot = totient(10**n)
    exponent = exp % tot
    return base ** exponent % 10**n

digits = []
num_digits = 10
for i in range(1000):
    val = i + 1
    if val % 10 == 0:
        pass
    digits.append(find_last_n_digits(val, val, num_digits))

print(sum(digits) % 10**num_digits)
