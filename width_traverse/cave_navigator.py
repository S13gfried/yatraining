import math


def get_cave_layout():
    size = int(input())
    start_x, start_y, start_z = -1, -1, -1
    passable = {'#': -2,
                '.': -1,
                'S': -1}

    cave = [[[-2 for index1 in range(size + 2)] for index2 in range(size + 2)]]

    for height in range(size):
        layer = [[-2 for index in range(size + 2)]]
        input()  # skip 1 line
        for width in range(size):
            line = [-2]
            input_line = input()
            for length in range(size):
                line.append(passable[input_line[length]])
                if input_line[length] == 'S':
                    start_x, start_y, start_z = height + 1, width + 1, length + 1

            line.append(-2)
            layer.append(line)
        layer.append([-2 for index in range(size + 2)])
        cave.append(layer)
    cave.append([[-2 for index1 in range(size + 2)] for index2 in range(size + 2)])
    return cave, start_x, start_y, start_z


def traverse_3d(tilemap, start_x, start_y, start_z):
    front = [(start_x, start_y, start_z)]
    tilemap[start_x][start_y][start_z] = 0
    length = 1

    while len(front) > 0:
        new_front = []
        for front_tile in front:
            neighbors = [(front_tile[0] - 1, front_tile[1], front_tile[2]),
                         (front_tile[0] + 1, front_tile[1], front_tile[2]),
                         (front_tile[0], front_tile[1] - 1, front_tile[2]),
                         (front_tile[0], front_tile[1] + 1, front_tile[2]),
                         (front_tile[0], front_tile[1], front_tile[2] - 1),
                         (front_tile[0], front_tile[1], front_tile[2] + 1)]
            for neighbor in neighbors:
                if tilemap[neighbor[0]][neighbor[1]][neighbor[2]] == -1:
                    new_front.append(neighbor)
                    tilemap[neighbor[0]][neighbor[1]][neighbor[2]] = length
        front = new_front
        length += 1


cave, start_x, start_y, start_z = get_cave_layout()
# print(start_x, start_y, start_z)

traverse_3d(cave, start_x, start_y, start_z)

shortest = math.inf
for line in cave[1]:
    for tile in line:
        if tile >= 0:
            shortest = min(shortest, tile)

# for i in cave:
#     for j in i:
#         print(j)
#     print()

print(shortest)
