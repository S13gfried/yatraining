stations = int(input())
lines = int(input())

neighbors = {}

for line in range(lines):
    line_input = [int(item) for item in input().split()]
    for station in range(len(line_input) - 3):
        neighbors[(line + 1, line_input[station + 2])] = [(line + 1, line_input[station + 1]), (line + 1, line_input[station + 3])]
        for other_line in range(line):
            if (other_line + 1, line_input[station + 2]) in neighbors:
                neighbors[(other_line + 1, line_input[station + 2])].append((line + 1, line_input[station + 2]))
                neighbors[(line + 1, line_input[station + 2])].append((other_line + 1, line_input[station + 2]))

    neighbors[(line + 1, line_input[1])] = [(line + 1, line_input[2])]
    for other_line in range(line):
        if (other_line + 1, line_input[1]) in neighbors:
            neighbors[(other_line + 1, line_input[1])].append((line + 1, line_input[1]))
            neighbors[(line + 1, line_input[1])].append((other_line + 1, line_input[1]))

    neighbors[(line + 1, line_input[-1])] = [(line + 1, line_input[-2])]
    for other_line in range(line):
        if (other_line + 1, line_input[-1]) in neighbors:
            neighbors[(other_line + 1, line_input[-1])].append((line + 1, line_input[-1]))
            neighbors[(line + 1, line_input[-1])].append((other_line + 1, line_input[-1]))

source, destination = tuple(int(item) for item in input().split())
visited = {key: -1 for key in neighbors.keys()}
front = []

for key in neighbors.keys():
    if key[1] == source:
        front.append(key)
        visited[key] = 0

length = 1

while len(front) > 0:
    new_front = []
    for front_station in front:
        for neighbor in neighbors[front_station]:
            if neighbor[0] == front_station[0] and (visited[neighbor] > length - 1 or visited[neighbor] == -1):
                visited[neighbor] = length - 1
                front.append(neighbor)
            if neighbor[0] != front_station[0] and visited[neighbor] == -1:
                visited[neighbor] = length
                new_front.append(neighbor)
    front = new_front
    length += 1

dest_options = []

for item in visited.items():
    if item[0][1] == destination:
        dest_options.append(item[1])

print(min(dest_options))
