def bridge_finder(graph: dict[int, list[int]]) -> list[tuple[int, int]]:
    if not graph:
        return []

    tin = {}
    low = {}
    timer = 0
    bridges = []
    visited = set()

    def dfs(u, p=-1):
        nonlocal timer
        visited.add(u)
        tin[u] = low[u] = timer
        timer += 1

        for v in graph.get(u, []):
            if v == p:
                continue
            if v in visited:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append((min(u, v), max(u, v)))

    for node in graph:
        if node not in visited:
            dfs(node)

    bridges.sort()
    return bridges
