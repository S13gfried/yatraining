def scan_graph():
    vertex_count, edge_count = tuple(int(item) for item in input().split())

    connections = [[] for i in range(vertex_count + 1)]

    for i in range(edge_count):
        edge = tuple(int(item) for item in input().split())
        if edge[0] != edge[1] and not edge[1] in connections[edge[0]]:  # do not include excessive edges
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])

    return vertex_count, edge_count, connections


def traverse_color(connections, visited, start=1):
    color = 1
    visited[start] = color

    vstack = [start]
    while len(vstack) > 0:
        terminal = True
        for neighbor in connections[vstack[-1]]:
            if visited[neighbor] == color:
                return False
        for neighbor in connections[vstack[-1]]:
            if visited[neighbor] == 0:
                color = 3 - color
                visited[neighbor] = color
                vstack.append(neighbor)
                terminal = False
                break
        if terminal:
            vstack.pop()
            color = 3 - color

    return True


vertex_count, edge_count, connections = scan_graph()
visited = [0 for i in range(len(connections))]

is_possible = True
for start in range(1, vertex_count + 1):
    if visited[start] == 0:
        if not traverse_color(connections, visited, start):
            is_possible = False
            break

print("YES" if is_possible else "NO")
