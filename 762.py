from collections import deque

while True:
    try:
        no_of_nodes = int(input())
        node_u = []
        node_v = []
        vertex_name = {}
        counter = 0

        for _ in range(no_of_nodes):
            u, v = map(str, input().split())
            node_u.append(u)
            node_v.append(v)

            if u not in vertex_name:
                counter += 1
                vertex_name[u] = counter
                    
            if v not in vertex_name:
                counter += 1
                vertex_name[v] = counter

        graph = [[0] * (counter + 1) for _ in range(counter + 1)]
        
        for i in range(no_of_nodes):
            u = vertex_name[node_u[i]]
            v = vertex_name[node_v[i]]
        
            graph[u][v] = 1
            graph[v][u] = 1

        src, des = map(str, input().split())
        print()

        bfs = deque()
        visited = list()
        for _ in range(counter+1):
            visited.append(False)
        bfs.append(src)
        visited[src] = True

        while bfs:
            node = bfs.popleft()
        
            for v in range(1, counter + 1):
        
                if graph[u][v] == 1 and distance[v] == -1:
                    if distance[u] + 1 <= ttl:
                        distance[v] = distance[u] + 1
                        bfs.append(v)

            
        
            

    except EOFError:
        break