def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    if not grid or not grid[0] or not pattern:
        return []
    
    rows = len(grid)
    cols = len(grid[0])
    pattern_len = len(pattern)
    
    # Define the 8 directions mapping (dx, dy) -> direction_code
    # Note: x corresponds to column index, y corresponds to row index.
    # Therefore, delta x (dx) is column offset, delta y (dy) is row offset.
    directions = [
        (1, 0, "H"),       # Horizontal right
        (-1, 0, "H-"),     # Horizontal left
        (0, 1, "V"),       # Vertical down
        (0, -1, "V-"),     # Vertical up
        (1, 1, "D1"),      # Diagonal down-right
        (-1, -1, "D1-"),   # Diagonal up-left
        (-1, 1, "D2"),     # Diagonal up-right
        (1, -1, "D2-")     # Diagonal down-left
    ]
    
    matches = []
    
    # Scan every cell (y, x) in the grid
    for y in range(rows):
        for x in range(cols):
            # Try each of the 8 directions from the starting cell (x, y)
            for dx, dy, code in directions:
                match = True
                for i in range(pattern_len):
                    ny, nx = y + i * dy, x + i * dx
                    # Check bounds and character match
                    if not (0 <= ny < rows and 0 <= nx < cols) or grid[ny][nx] != pattern[i]:
                        match = False
                        break
                
                if match:
                    matches.append((x, y, code))
                    
    return matches
