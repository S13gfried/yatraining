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


def traverse_cycle(connections, visited, start = 1):

    visited[start] = 1
    cycle = []
    # print("begin []")
    vstack = [start]
    while len(vstack) > 0:
        terminal = True

        collision = False
        for neighbor in connections[vstack[-1]]:
            # print("testing ", neighbor, " ", vstack[-1])
            if visited[neighbor] == 1 and neighbor != vstack[-2]:
                # print("collision ", vstack[-2], neighbor)
                loop = neighbor
                while True:
                    cycle.append(vstack.pop())
                    # print(cycle)

                    if cycle[-1] == loop:
                        break
                return cycle

        for neighbor in connections[vstack[-1]]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                vstack.append(neighbor)
                # print(vstack)
                # print(visited)
                terminal = False
                break
        if terminal:
            visited[vstack[-1]] = 2
            vstack.pop()
            # print(vstack)
            # print(visited)

    return cycle


vertex_count, edge_count, connections = scan_graph_matrix()

cycle = []
cycle_found = False
visited = [0 for i in range(vertex_count + 1)]
for vertexno in range(1, vertex_count+1):
    if visited[vertexno] == 0:
        cycle = traverse_cycle(connections, visited, vertexno)
        if len(cycle) > 0:
            cycle_found = True
            break

if cycle_found:
    print("YES")
    print(len(cycle))
    print(" ".join(str(vertex) for vertex in cycle))
else:
    print("NO")
