import math
target_sum = 1000.000
flag = True
a = 1
b = 0
c = 0

while flag:
    for b in range(a,math.floor(target_sum/2)):
        
        c = math.sqrt(a*a + b*b)
        if c.is_integer() and a+b+c == target_sum:
            flag = False
            break
        
    a+=1

print(a-1,b,int(c),int((a-1)*b*c))