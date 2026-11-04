def island_matrix_counter(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    num_islands = 0
    
    def dfs(r, c):
        # Out of bounds, water ("0"), or already visited
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] == "0" or (r, c) in visited:
            return
        
        visited.add((r, c))
        
        # Traverse all 4 cardinal directions (horizontally and vertically)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell ("1"), it's the start of a new island
            if matrix[r][c] == "1" and (r, c) not in visited:
                num_islands += 1
                dfs(r, c)
                
    return num_islands
