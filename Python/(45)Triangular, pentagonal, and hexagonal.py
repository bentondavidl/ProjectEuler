import math


def is_pentag(n: int) -> bool:
    val = (math.sqrt(24*n + 1) + 1)/6
    return math.floor(val) == val


i = 143
while True:
    i += 1
    num = i * (2*i-1)
    if is_pentag(num):
        print(num)
        exit()
