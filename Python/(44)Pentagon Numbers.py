def solve():
    pentags = set()
    i = 1000
    while True:
        i += 1
        s = (3*i*i - i) // 2
        for Pj in pentags:
            if s-Pj in pentags and s-2*Pj in pentags: 
                return s-2*Pj
        pentags.add(s)

print(solve())