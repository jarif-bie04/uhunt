from collections import deque

case = 1

while True:
    number_of_edges = int(input())

    if number_of_edges == 0:
        break

    node_u = []
    node_v = []
    vertex_name = {}
    counter = 0

    for _ in range(number_of_edges):
        u, v = map(int, input().split())

        node_u.append(u)
        node_v.append(v)

        if u not in vertex_name:
            counter += 1
            vertex_name[u] = counter

        if v not in vertex_name:
            counter += 1
            vertex_name[v] = counter

    graph = [[0] * (counter + 1) for _ in range(counter + 1)]

    for i in range(number_of_edges):
        u = vertex_name[node_u[i]]
        v = vertex_name[node_v[i]]

        graph[u][v] = 1
        graph[v][u] = 1

    while True:
        src, ttl = map(int, input().split())

        if src == 0 and ttl == 0:
            break

        if src not in vertex_name:
            unvisited = counter

        else:
            source = vertex_name[src]
            distance = [-1] * (counter + 1)

            bfs = deque()

            bfs.append(source)
            distance[source] = 0
            while bfs:
                u = bfs.popleft()

                for v in range(1, counter + 1):

                    if graph[u][v] == 1 and distance[v] == -1:
                        if distance[u] + 1 <= ttl:
                            distance[v] = distance[u] + 1
                            bfs.append(v)

            visited = 0

            for i in range(1, counter + 1):
                if distance[i] != -1:
                    visited += 1

            unvisited = counter - visited

        print(
            f"Case {case}: {unvisited} "
            f"nodes not visited from node {src} with TTL = {ttl}."
        )

        case += 1