def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort by start time - O(n log n)
    intervals.sort(key=lambda x: x[0])

    merged = []
    
    for current in intervals:
        # If merged is empty or no overlap with the last interval
        # No overlap means: current start > last merged end
        if not merged or current[0] > merged[-1][1]:
            merged.append(current)
        else:
            # There is an overlap, merge by updating the end time
            # We take max() because the current interval could be "inside" the last one
            merged[-1][1] = max(merged[-1][1], current[1])
            
    return merged

# --- User Input Handling ---
if __name__ == "__main__":
    print("Enter intervals as pairs (e.g., 1,3 2,6 8,10):")
    try:
        user_input = input("> ").split()
        # Parsing: "1,3" -> [1, 3]
        intervals = [list(map(int, x.split(','))) for x in user_input]
        
        result = merge_intervals(intervals)
        print(f"Merged Intervals: {result}")
    except Exception as e:
        print(f"Invalid format. Use 'start,end' separated by spaces. Error: {e}")