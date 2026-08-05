from collections import deque

# Function to generate possible next states
def get_next_states(state):
    a, b = state
    
    # Capacities of jugs
    jugA = 4
    jugB = 3
    
    states = []

    # Fill Jug A completely
    states.append((jugA, b))

    # Fill Jug B completely
    states.append((a, jugB))

    # Empty Jug A
    states.append((0, b))

    # Empty Jug B
    states.append((a, 0))

    # Pour water from A to B
    pour = min(a, jugB - b)
    states.append((a - pour, b + pour))

    # Pour water from B to A
    pour = min(b, jugA - a)
    states.append((a + pour, b - pour))

    return states


# BFS implementation
def bfs():

    start = (0, 0)
    goal = 2

    # Queue for BFS
    queue = deque()

    # Store state and path
    queue.append((start, []))

    # To avoid visiting same states
    visited = set()

    while queue:

        current, path = queue.popleft()

        a, b = current

        # If goal found
        if a == goal:
            return path + [current]

        # Mark state visited
        if current in visited:
            continue

        visited.add(current)

        # Generate child states
        for next_state in get_next_states(current):

            if next_state not in visited:
                queue.append(
                    (next_state, path + [current])
                )

    return None


# Run BFS
solution = bfs()

print("Steps to reach goal:")

for step in solution:
    print(step)
