def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    if not graph:
        return False
    
    # States: 0 = unvisited, 1 = visiting (currently in path), 2 = visited (fully processed)
    state = {}
    
    def dfs(node: int) -> bool:
        # If node is currently in the recursion stack, we found a cycle
        if state.get(node, 0) == 1:
            return True
        # If already fully processed, no cycle down this path
        if state.get(node, 0) == 2:
            return False
        
        # Mark as currently visiting
        state[node] = 1
        
        # Visit all neighbors
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
                
        # Mark as fully processed (safe)
        state[node] = 2
        return False

    # Check every node in case the graph has disconnected components
    for node in graph:
        if state.get(node, 0) == 0:
            if dfs(node):
                return True
                
    return False
