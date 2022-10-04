from queue import PriorityQueue


def convert_to_adj(size, edges):
    graph = [[] for _ in range(size)]
    for u, v, w in edges:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    return graph


def lowest(size, edges):
    source, target = 0, 1
    graph = convert_to_adj(size, edges)

    parent = [None for _ in range(size)]
    dist = [0 for _ in range(size)]
    visited = [False for _ in range(size)]
    queue = PriorityQueue()

    dist[source] = float("inf")
    queue.put((-dist[source], source))
    while not queue.empty():
        d, u = queue.get()
        d = -d
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                old_max = dist[v]
                new_max = min(dist[u], w)
                if new_max > old_max:
                    dist[v] = new_max
                    parent[v] = u
                    queue.put((-dist[v], v))
    return dist[target]
