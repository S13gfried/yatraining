def traverse_width(visited, getNeighbors, destination=1, start=1, not_visited=-1):
    front = [start]
    visited[start] = 0
    distance = 1
    while len(front) > 0:
        nfront = []
        for fvertex in front:
            for neighbor in getNeighbors(fvertex):
                if visited[neighbor] == not_visited:
                    nfront.append(neighbor)
                    visited[neighbor] = distance
        front = nfront
        distance += 1
    return visited[destination]

def index_flat(width, x, y):
    return width*y + (x % width)


def index_spatial(width, flat):
    return flat % width, flat // width


width, height, target_x, target_y, flea_count = tuple(int(item) for item in input().split())

fleas = []
for i in range(flea_count):
    fleas.append(tuple(int(item) for item in input().split()))


def is_border(width, height, index):
    spatial = index_spatial(width, index)
    is_vertical_border = spatial[0] == width - 1 or spatial[0] == 0
    is_horizontal_border = spatial[1] == height - 1 or spatial[1] == 0
    return is_horizontal_border or is_vertical_border


visited = [-2 if is_border(width + 2, height + 2, index) else -1 for index in range((width + 2)*(height + 2))]


def get_knight_move_codes(x, y, encode):
    moves = [(x - 1, y - 2),
             (x - 1, y + 2),
             (x + 1, y - 2),
             (x + 1, y + 2),
             (x - 2, y - 1),
             (x - 2, y + 1),
             (x + 2, y - 1),
             (x + 2, y + 1)]
    return list(encode(move) for move in moves)


def get_grid_neighbours_knight(index):
    spatial = index_spatial(width + 2, index)
    codes_raw = get_knight_move_codes(spatial[0], spatial[1], lambda x: index_flat(width + 2, x[0], x[1]))
    return (item % ((width + 2)*(height + 2)) for item in codes_raw)


traverse_width(visited, get_grid_neighbours_knight, 1, index_flat(width + 2, target_x, target_y))

totalPath = 0
for flea in fleas:
    if visited[index_flat(width + 2, flea[0], flea[1])] == -1:
        totalPath = -1
        break
    totalPath += visited[index_flat(width + 2, flea[0], flea[1])]

print(totalPath)
