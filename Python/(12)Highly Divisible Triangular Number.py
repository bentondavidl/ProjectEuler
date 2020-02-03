import math

target_number = 5
index = 0


while True:
    index += 1
    triangle_number = 0
    for i in range(1,index+1):
        triangle_number += i
    
    num = triangle_number
    factors = []

    while triangle_number % 2 == 0:
        factors.append(2)
        triangle_number /= 2
    for i in range(3, math.floor(math.sqrt(triangle_number)), 2):
        while triangle_number % i == 0:
            factors.append(i)
            triangle_number /= i

    num_factors = {}
    for n in factors:
        try: 
            num_factors[n] += 1
        except:
            num_factors[n] = 1

    tot_factors = 1
    for n in num_factors.values():
        tot_factors *= n+1

    if(tot_factors >= 500):
        print(num, tot_factors)
        print(factors)
        break
    