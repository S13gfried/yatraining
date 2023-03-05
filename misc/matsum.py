height, width, queries = (int(word) for word in input().split())
cmatrix = []

for row in range(height):
    newrow = []
    inputs = [int(word) for word in input().split()]
    newrow.append(inputs[0])

    for column in range(width - 1):
        newrow.append(inputs[column + 1] + newrow[column])

    cmatrix.append(newrow)

for row in range(height - 1):
    for column in range(width):
        cmatrix[row + 1][column] = cmatrix[row + 1][column] + cmatrix[row][column]

for i in range(queries):
    x2, y1, x1, y2  = (int(word) - 1 for word in input().split())

    sum = cmatrix[x1][y2]

    if y1 > 0:
        sum = sum - cmatrix[x1][y1-1]
    if x2 > 0:
        sum = sum - cmatrix[x2-1][y2]

        if y1 > 0:
            sum = sum + cmatrix[x2-1][y1-1]
    print(int(sum))