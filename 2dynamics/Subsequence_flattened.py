length1 = int(input())
sequence1 = [int(item) for item in input().split()]

length2 = int(input())
sequence2 = [int(item) for item in input().split()]

solution = [0 for j in range((length1 + 1)*(length2 + 1)*2)]


def access_element(i, j, k):
    return ((length2 + 1)*i + j)*2 + k


for index1 in range(length1):
    for index2 in range(length2):

        if sequence1[index1] != sequence2[index2]:
            if solution[access_element(index1, index2 + 1, 0)] > solution[access_element(index1 + 1, index2, 0)]:
                solution[access_element(index1 + 1, index2 + 1, 0)] = solution[access_element(index1, index2 + 1, 0)]
                solution[access_element(index1 + 1, index2 + 1, 1)] = 1
            else:
                solution[access_element(index1 + 1, index2 + 1, 0)] = solution[access_element(index1 + 1, index2, 0)]
                solution[access_element(index1 + 1, index2 + 1, 1)] = 2

        else:
            solution[access_element(index1 + 1, index2 + 1, 0)] = solution[access_element(index1, index2, 0)] + 1
            solution[access_element(index1 + 1, index2 + 1, 1)] = 3

res = []
directions = {1: [-1, 0],
              2: [0, -1],
              3: [-1, -1]}
index1, index2, direction = length1, length2, solution[access_element(length1, length2, 1)]
while direction != 0:
    if direction == 3:
        res.append(sequence1[index1 - 1])
    index1 += directions[direction][0]
    index2 += directions[direction][1]
    direction = solution[access_element(index1, index2, 1)]

res.reverse()
print(" ".join([str(item) for item in res]))
