a_max = 100
b_max = 100

pows = set()
for a in range(2, a_max+1):
    for b in range(2, b_max+1):
        pows.add(a**b)

print(len(pows))
