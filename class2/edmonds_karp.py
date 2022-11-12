from queue import Queue
# The following is an implementation of the ford-fulkerson network flow algorithm.


def bfs(graph, parent, source, sink):
    visited = [False for _ in graph]
    queue = Queue()
    visited[source] = True
    queue.put(source)

    while not queue.empty():
        u = queue.get()
        for v in range(0, len(graph)):
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
                if v == sink:
                    return True

    return False


def EdmondsKarp(edges, size):
    graph = convert_to_matrix(size, edges)
    source, sink = 0, size - 1
    parent = [None for _ in graph]
    max_flow = 0

    while bfs(graph, parent, source, sink):
        path_flow = float("inf")
        curr = sink
        while curr != source:
            path_flow = min(path_flow, graph[parent[curr]][curr])
            curr = parent[curr]
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u

    return max_flow


def convert_to_matrix(size, edges):
    graph = [[0 for _ in range(size)] for _ in range(size)]
    for u, v, w in edges:
        graph[u-1][v-1] = w
    return graph
