import math
palindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        temp = str(i*j)
        if temp[:math.floor(len(temp)/2)] == temp[math.floor(len(temp)/2):][::-1]:
            if int(temp) > palindrome:
                palindrome = int(temp)

print(palindrome)