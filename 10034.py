def node_distance(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def find(parent, i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]
        i = parent[i]
    return parent[i]


def kruskals_algo(node_dis, node):
    node_dis.sort()
    total = 0.0
    taken = 0
    for dis, i, j in node_dis:
        root_i, root_j = find(parent, i), find(parent, j)
        if root_i != root_j:
            parent[root_i] = root_j
            total += dis
            taken += 1
            if taken == node - 1:
                break
    return total

t_case = int(input())
for tc in range(t_case):
    input()
    node = int(input())
    parent = list(range(node))
    node_pos = list()
    for i in range(node):
        x, y = map(float, input().split())
        node_pos.append((x,y))
    node_dis = list()
    for i in range(node):
        for j in range(i+1, node):
            node_dis.append((node_distance(node_pos[i], node_pos[j]), i, j))

    if tc > 0:
        print()
    print(f"{kruskals_algo(node_dis, node):.2f}")