from collections import deque

def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    # 1. Validation checks
    if len(start) != len(end):
        return 0
        
    word_set = set(sentence)
    if end not in word_set:
        return 0
        
    if start == end:
        return 1
        
    # 2. BFS to find the shortest transformation ladder
    queue = deque([(start, 1)])
    visited = {start}
    
    while queue:
        current_word, length = queue.popleft()
        
        if current_word == end:
            return length
            
        # Try changing each character one by one (a-z)
        for i in range(len(current_word)):
            original_char = current_word[i]
            for char_code in range(ord('a'), ord('z') + 1):
                c = chr(char_code)
                if c == original_char:
                    continue
                    
                next_word = current_word[:i] + c + current_word[i+1:]
                
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
                    
    return 0