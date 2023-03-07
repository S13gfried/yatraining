import math
height, width = tuple(int(item) for item in input().split())

matrix = [[int(item) for item in input().split()] for i in range(height)]

solution = [[0 for i in range(width + 1)] for j in range(height + 1)]

for i in range(width - 1):
    solution[0][i + 2] = math.inf
for i in range(height):
    solution[i + 1][0] = math.inf

for row in range(height):
    for col in range(width):
        solution[row + 1][col + 1] = min(solution[row][col + 1], solution[row + 1][col]) + matrix[row][col]

print(solution[-1][-1])
