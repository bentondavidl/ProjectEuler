pow = 5
start_value = 1000
current_number = start_value
current_sum = 0
last_match = 0

sum_of_pows = []

while True:
    current_number += 1
    if current_number - last_match > 1000000:
        break
    pows = []
    for digit in str(current_number):
        pows.append(int(digit) ** pow)
    current_sum = sum(pows)

    if current_sum == current_number:
        sum_of_pows.append(current_number)
        last_match = current_number
        print("found ", current_number)

print(sum(sum_of_pows))
