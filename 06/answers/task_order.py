import heapq


def task_order(n: int, prereqs: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(n)]
    in_degree = [0] * n

    # Build adjacency list and calculate in-degrees
    # [a, b] means b must be completed before a (edge: b -> a)
    for a, b in prereqs:
        adj[b].append(a)
        in_degree[a] += 1

    # Initialize heap with all tasks having 0 prerequisites
    heap = [i for i in range(n) if in_degree[i] == 0]
    heapq.heapify(heap)

    order = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)

        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    # If we couldn't schedule all tasks, there is a cycle
    if len(order) != n:
        return []

    return order
