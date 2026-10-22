def compress(s: str) -> str:
    if not s:
        return ""
    
    compressed_chars = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        count = 0
        
        # Count consecutive identical characters
        while i < n and s[i] == char:
            count += 1
            i += 1
            
        compressed_chars.append(char)
        # Omit '1' if the character appears only once consecutively
        if count > 1:
            compressed_chars.append(str(count))
            
    return "".join(compressed_chars)


def decompress(s: str) -> str:
    if not s:
        return ""
    
    decompressed_chars = []
    i = 0
    n = len(s)
    
    while i < n:
        char = s[i]
        i += 1
        
        # Parse potential multi-digit counts following the character
        num_str = ""
        while i < n and s[i].isdigit():
            num_str += s[i]
            i += 1
            
        count = int(num_str) if num_str else 1
        decompressed_chars.append(char * count)
        
    return "".join(decompressed_chars)
