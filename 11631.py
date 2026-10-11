import  sys
input = sys.stdin.readline

parent = list()
rank = list()

def make(v):
    parent.append(v)
    rank.append(0)

def find(v):
    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]
    return v

def union(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    if rank[u] < rank[v]:
        u, v = v, u
    parent[v] = u
    if rank[u] == rank[v]:
        rank[u] += 1
    return True

while True:
    try:
        no_of_node, no_of_edge = list(map(int, input().split()))
        if no_of_node == 0 and no_of_edge == 0:
            break
        edges = list()
        total_cost = 0
        for i in range(no_of_edge):
            u, v, wt = list(map(int, input().split()))
            edges.append((wt, u, v))
            total_cost += wt

        parent.clear()
        rank.clear()

        edges.sort()
        cost = 0

        for i in range(no_of_node):
            make(i)

        for edge in edges:
            wt = edge[0]
            u = edge[1]
            v = edge[2]
            if union(u, v):
                cost += wt

        print(total_cost-cost)

    except (EOFError, ValueError):
        break