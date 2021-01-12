top = 1000
tot = 0
for i in range(top):
    if(i % 3 == 0 or i % 5 == 0):
        tot += i

print(tot)