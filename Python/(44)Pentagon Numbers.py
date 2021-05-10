def n_pentagonal(n):
    return int(n*(3*n-1)/2)

pentags = []
for i in range(1, 100000):
    pentags.append(n_pentagonal(i))

flag = True
slow = 0
p_set = set(pentags)
found = -1
while flag and slow < len(pentags):
    for i in range(slow+1, len(pentags)):
        if (res:=pentags[i] + pentags[slow] in p_set) and (res + pentags[i] in p_set):
            flag = False
            found = pentags[slow]
            break
    slow += 1
    
print(found)