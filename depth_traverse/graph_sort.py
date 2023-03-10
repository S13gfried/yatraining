def scan_graph_oriented():
    vertex_count, edge_count = tuple(int(item) for item in input().split())

    connections = [[] for i in range(vertex_count + 1)]

    for i in range(edge_count):
        edge = tuple(int(item) for item in input().split())
        if not edge[1] in connections[edge[0]]:  # do not include excessive edges
            connections[edge[0]].append(edge[1])

    return vertex_count, edge_count, connections


def traverse_sort(connections, visited, start=1):
    visited[start] = 1
    sorted = []

    vstack = [start]
    while len(vstack) > 0:

        terminal = True

        for neighbor in connections[vstack[-1]]:
            if visited[neighbor] == 1:
                return []

        for neighbor in connections[vstack[-1]]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                vstack.append(neighbor)
                terminal = False
                break

        if terminal:
            visited[vstack[-1]] = 2
            sorted.append(vstack.pop())

    return sorted


vertex_count, edge_count, connections = scan_graph_oriented()
visited = [0 for i in range(len(connections))]

sorted_final = []
is_possible = True

for start in range(1, vertex_count + 1):
    if visited[start] == 0:
        addition = traverse_sort(connections, visited, start)
        if len(addition) == 0:
            is_possible = False
            break
        sorted_final.extend(addition)

if is_possible:
    print(" ".join([str(item) for item in sorted_final[::-1]]))
else:
    print(-1)
