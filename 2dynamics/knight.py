height, width = tuple(int(item) for item in input().split())

solution = [[0 for i in range(width + 2)] for j in range(height + 2)]

solution[0][1] = 1

for row in range(height):
    for col in range(width):
        solution[row + 2][col + 2] = solution[row][col + 1] + solution[row + 1][col]

print(solution[-1][-1])
