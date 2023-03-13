import numpy as np
height, width, queries = (int(word) for word in input().split())

cmatrix = np.zeros((height, width))

for row in range(height):
    inputs = [int(word) for word in input().split()]
    for column in range(width):
        cmatrix[row][column] = inputs[column] + cmatrix[row][column-1]

for row in range(height - 1):
    cmatrix[row + 1] = cmatrix[row + 1] + cmatrix[row]

for i in range(queries):
    x2, y1, x1, y2 = (int(word) - 1 for word in input().split())

    sum = cmatrix[x1][y2]

    if y1 > 0:
        sum = sum - cmatrix[x1][y1-1]
    if x2 > 0:
        sum = sum - cmatrix[x2-1][y2]

        if y1 > 0:
            sum = sum + cmatrix[x2-1][y1-1]
    print(int(sum))