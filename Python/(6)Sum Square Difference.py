max_number = 100
sum_squares = 0
square_sums = 0

for i in range(max_number+1):
    sum_squares += i*i
    square_sums += i
square_sums *= square_sums

print(square_sums - sum_squares)