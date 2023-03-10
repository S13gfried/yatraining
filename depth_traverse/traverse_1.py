def scan_graph():
    vertex_count, edge_count = tuple(int(item) for item in input().split())

    connections = [[] for i in range(vertex_count + 1)]

    for i in range(edge_count):
        edge = tuple(int(item) for item in input().split())
        if edge[0] != edge[1] and not edge[1] in connections[edge[0]]:  # do not include excessive edges
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])

    return vertex_count, edge_count, connections


def traverse_connectivity(connections, start = 1):
    visited = [0 for i in range(len(connections) + 1)]
    visited[start] = 1
    domain = [start]

    vstack = [start]
    while len(vstack) > 0:
        terminal = True
        for neighbor in connections[vstack[-1]]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                vstack.append(neighbor)
                domain.append(neighbor)
                terminal = False
                break
        if terminal:
            vstack.pop()
    return domain


vertex_count, edge_count, connections = scan_graph()
domain = traverse_connectivity(connections, 1)

domain.sort()
print(len(domain))
print(" ".join([str(item) for item in domain]))
