class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False


def redundant_link(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    dsu = DSU(n)

    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]

    return []
