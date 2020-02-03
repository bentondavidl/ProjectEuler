import math

grid_x = 20
grid_y = 20

total_paths = math.factorial(grid_x+grid_y) / math.factorial(grid_x)**2

print(total_paths)

