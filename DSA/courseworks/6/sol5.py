def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    new_start, new_end = newInterval

    # Phase 1: Add all intervals that end before the new one starts
    while i < n and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1

    # Phase 2: Merge overlapping intervals
    # Overlap exists as long as the current interval starts before the new one ends
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1
    
    # Add the final merged version of the new interval
    result.append([new_start, new_end])

    # Phase 3: Add all remaining intervals that start after the new one ends
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

# --- User Input Handling ---
if __name__ == "__main__":
    print("Enter existing intervals (e.g., 1,3 6,9):")
    try:
        raw_intervals = input("> ").split()
        intervals = [list(map(int, x.split(','))) for x in raw_intervals]
        
        print("Enter new interval (e.g., 2,5):")
        new_interval_raw = input("> ").split(',')
        new_interval = [int(new_interval_raw[0]), int(new_interval_raw[1])]
        
        result = insert_interval(intervals, new_interval)
        print(f"Updated Intervals: {result}")
    except Exception as e:
        print(f"Input error: Ensure format is 'start,end' and intervals are sorted. {e}")