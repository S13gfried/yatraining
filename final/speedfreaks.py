import copy

height, width = tuple(int(item) for item in input().split())

rotation_layer = [[-2 for i in range(width + 2)]]
encoding = {'X': -2, '.': -1}
for i in range(height):
    line = [-2]
    for char in input():
        line.append(encoding[char])
    line.append(-2)
    rotation_layer.append(line)
rotation_layer.append([-2 for i in range(width + 2)])

visited = list(copy.deepcopy(rotation_layer) for i in range(8))

directions = [(0, 1),
              (1, 1),
              (1, 0),
              (1, -1),
              (0, -1),
              (-1, -1),
              (-1, 0),
              (-1, 1)]

# (dir, y(height), x(width))
source_y, source_x = tuple(int(item) for item in input().split())
destination_y, destination_x = tuple(int(item) for item in input().split())

source_x = height - source_x + 1
destination_x = height - destination_x + 1

front = []
for i in range(0, 8):
    front.append((i, source_x, source_y))
    visited[i][source_x][source_y] = 0

length = 1
while len(front) > 0:
    new_front = []
    for front_position in front:
        # print("\nfp: ", front_position)
        # turns
        for i in range(8):
            status = max(visited[j][front_position[1] + directions[i][0]][
                front_position[2] + directions[i][1]] for j in range(8))
            # print (visited[i][front_position[1] + directions[i][0]][front_position[2] + directions[i][1]])
            if front_position[0] != i and visited[i][front_position[1]][front_position[2]] == -1 and status == -1: #!!
                visited[i][front_position[1]][front_position[2]] = length
                new_front.append((i, front_position[1], front_position[2]))
                # print("appended back ", (i, front_position[1], front_position[2]))

        # forward
        direction = front_position[0]
        status = visited[direction][front_position[1] + directions[direction][0]][
            front_position[2] + directions[direction][1]]

        if status == -1 or status > length - 1:
            front.append(
                (direction, front_position[1] + directions[direction][0], front_position[2] + directions[direction][1]))
            visited[direction][front_position[1] + directions[direction][0]][
                front_position[2] + directions[direction][1]] = length - 1
            if (front_position[1] + directions[direction][0] == destination_x and
                front_position[2] + directions[direction][1]) == destination_y:
                    break
            # print("appended ", (
            # direction, front_position[1] + directions[direction][0], front_position[2] + directions[direction][1]))

    # print(len(front))
    front = new_front
    length += 1

options = [visited[i][destination_x][destination_y] for i in range(8)]
options_new = [option if option >= 0 else 100000000 for option in options]
best = min(options_new)
if best == 100000000:
    print(-1)
else:
    print(best + 1)
