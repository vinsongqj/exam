def generate_spiral(n: int) -> list[list[int]]:
    if n <= 0:
        return []
    
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    
    while num <= n * n:
        # 1. Traverse from left to right along the top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # 2. Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # 3. Traverse from right to left along the bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        # 4. Traverse from bottom to top along the left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
        
    return matrix
