import copy
height, width = tuple(int(item) for item in input().split())

matrix = [[int(item) for item in input().split()] for i in range(height)]

solution = [[[0, []] for i in range(width + 1)] for j in range(height + 1)]

# for i in range(width + 1):
#     solution[0][i][0] = 0
# for i in range(height):
#     solution[i + 1][0][0] = 0

for row in range(height):
    for col in range(width):
        if solution[row + 1][col] > solution[row][col + 1]:
            optimum, step = solution[row + 1][col], "R"
        else:
            optimum, step = solution[row][col + 1], "D"

        solution[row + 1][col + 1] = copy.deepcopy(optimum)
        solution[row + 1][col + 1][0] += matrix[row][col]
        solution[row + 1][col + 1][1].append(step)

print(solution[-1][-1][0])
print(" ".join([str(item) for item in solution[-1][-1][1][1:]]))
