max_side_length = 1001
diagonal_sum = 0

for i in range(3, max_side_length+1, 2):
    side_len = (i*i - (i-2)*(i-2))//4
    diagonal_sum += i*i + (i*i - side_len) + \
        (i*i - 2*side_len) + (i*i - 3*side_len)

print(diagonal_sum+1)
