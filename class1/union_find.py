def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x == root_y:
        return

    if rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        if rank[root_x] == rank[root_y]:
            rank[root_y] += 1


def lowest(size, edges):
    s, t = 1, 2
    edges.sort(key=lambda x: -x[2])
    parent = [i for i in range(size+1)]
    rank = [0 for i in range(size+1)]
    minimum = float("inf")
    for u, v, w in edges:  # O(Elog(V))
        if find(s, parent) == find(t, parent):
            break
        union(u, v, parent, rank)  # O(log(V))
        minimum = min(minimum, w)
    return minimum
