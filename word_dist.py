import heapq
import enchant
import sys
import string

def get_neighbors(word, dictionaries):
    neighbors = set()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(word)):
        for char in alphabet:
            if char != word[i]:
                neighbor = word[:i] + char + word[i+1:]
                # Check against all dictionaries provided
                for d in dictionaries:
                    if d.check(neighbor):
                        neighbors.add(neighbor)
                        
    return list(neighbors)

def find_shortest_word_path(start, end, dicts):
    # Min-priority queue storing tuples: (distance, current_word, path_so_far)
    queue = [(0, start, [start])]
    visited = {start: 0}

    while queue:
        current_dist, current_word, path = heapq.heappop(queue)

        # Target reached
        if current_word == end:
            return path

        # Skip if we've already found a shorter path to this word
        if current_dist > visited[current_word]:
            continue

        for neighbor in get_neighbors(current_word, dicts):
            new_dist = current_dist + 1
            
            # If a shorter path to neighbor is found
            if neighbor not in visited or new_dist < visited[neighbor]:
                visited[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor, path + [neighbor]))

    return None  # Return None if no valid path exists

# Execution
dicts = (enchant.Dict("en_UK"), enchant.Dict("en_US"), enchant.Dict("de_DE"))

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: word_dist.py <start_word> <end_word>")
        sys.exit(1)
    
    start = sys.argv[1]
    end = sys.argv[2]

    assert len(start) == len(end)

    start_valid_word = False
    end_valid_word = False
    for d in dicts:
        if d.check(start):
            start_valid_word = True
        if d.check(end):
            end_valid_word = True
    
    if not start_valid_word:
        print(f"Error: start_word was not found in dict:")
        print([d.tag for d in dicts])
    if not end_valid_word:
        print(f"Error: end_word was not found in dict:")
        print([d.tag for d in dicts])
    
    path = find_shortest_word_path(start, end, dicts)
    
    if path:
        print(f"Shortest path ({len(path) - 1} steps): {' -> '.join(path)}")
    else:
        print("No valid path found.")
