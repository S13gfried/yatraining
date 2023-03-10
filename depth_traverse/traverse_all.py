def scan_graph():
    vertex_count, edge_count = tuple(int(item) for item in input().split())

    connections = [[] for i in range(vertex_count + 1)]

    for i in range(edge_count):
        edge = tuple(int(item) for item in input().split())
        if edge[0] != edge[1] and not edge[1] in connections[edge[0]]:  # do not include excessive edges
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])

    return vertex_count, edge_count, connections


def traverse_connectivity(connections, visited, start = 1):
    visited[start] = visited[0] + 1
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

    visited[0] += 1
    return domain


vertex_count, edge_count, connections = scan_graph()
domains = []

visited = [0 for i in range(vertex_count + 1)]
for vertexno in range(1, vertex_count+1):
    if visited[vertexno] == 0:
        domains.append(traverse_connectivity(connections, visited, vertexno))

print(len(domains))
for domain in domains:
    print(len(domain))
    print(" ".join(str(vertex) for vertex in domain))
