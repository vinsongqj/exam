def schedule_meetings(intervals: list[tuple[int, int]]) -> tuple[int, list]:
    if not intervals:
        return (0, [])
    
    # Sort meetings by their start time
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    
    rooms = []          # Stores lists of assigned meeting intervals for each room
    room_end_times = [] # Stores the end time of the last meeting in each room
    
    for interval in sorted_intervals:
        start, end = interval
        assigned = False
        
        # Check existing rooms to see if any room is free
        for i in range(len(rooms)):
            if room_end_times[i] <= start:
                rooms[i].append(interval)
                room_end_times[i] = end
                assigned = True
                break
                
        # If no existing room is free, open a new room
        if not assigned:
            rooms.append([interval])
            room_end_times.append(end)
            
    return (len(rooms), rooms)
