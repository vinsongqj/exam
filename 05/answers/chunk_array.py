def chunkArray(arr: list, size: int) -> list[list]:
    if size <= 0 or not arr:
        return []
    
    res = []
    for i in range(0, len(arr), size):
        chunk = list(arr[i:i+size])  # Create a slice copy to avoid modifying the original list
        
        # Pad the last chunk with None if it is short
        if len(chunk) < size:
            chunk.extend([None] * (size - len(chunk)))
            
        res.append(chunk)
        
    return res