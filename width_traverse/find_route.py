def scan_graph_matrix():
    vertex_count = int(input())

    connections, edge_count = [[] for i in range(vertex_count + 1)], 0
    for line in range(vertex_count):
        edges = tuple(int(item) for item in input().split())

        for index in range(line, vertex_count):
            if edges[index] == 1:
                edge_count += 1

                connections[line + 1].append(index + 1)
                connections[index + 1].append(line + 1)

    return vertex_count, edge_count, connections


def traverse_width(visited, getNeighbors, destination=1, start=1, not_visited=-1):
    front = [start]
    distance = 0
    while len(front) > 0:
        for fvertex in front:
            visited[fvertex] = distance
        nfront = []
        for fvertex in front:
            for neighbor in getNeighbors(fvertex):
                if visited[neighbor] == not_visited:
                    nfront.append(neighbor)
        front = nfront
        distance += 1
    return visited[destination]

vertex_count, edge_count, connections = scan_graph_matrix()
source, destination = tuple(int(item) for item in input().split())

visited = [-1 for i in range(vertex_count + 1)]

print(traverse_width(visited, lambda x: connections[x], destination, source))