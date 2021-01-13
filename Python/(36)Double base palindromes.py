def check_palendrome(value) -> bool:
    if isinstance(value, str):
        value = value[2:]
    elif isinstance(value, int):
        value = str(value)

    for i in range(len(value)//2):
        if value[i] != value[len(value)-i-1]:
            return False

    return True


total = 0

for i in range(1, 1000000):
    if check_palendrome(i) and check_palendrome(bin(i)):
        total += i

print(total)
