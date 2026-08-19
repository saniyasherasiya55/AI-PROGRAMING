# 2.


from collections import deque
# deque() creates a double-ended queue.
# It allows fast insertion/removal from both ends.
# BFS uses it as a FIFO queue.


# Goal state; 0 represents the blank space
goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)


# Possible positions where the blank can move
# Positions are numbered as:
# 0 1 2
# 3 4 5
# 6 7 8
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}


# Function to find the shortest path using BFS
def bfs(start):

    # Create queue and store starting state with empty path
    queue = deque([(start, [])])

    # set() creates a set; used to store visited states
    visited = set([start])

    # Continue searching while queue is not empty
    while queue:

        # popleft() removes and returns the first item from the queue
        # This follows FIFO order required by BFS
        state, path = queue.popleft()

        # Check whether current state is the goal state
        if state == goal:

            # Return the path including the goal state
            return path + [state]

        # index() returns the position of the given value
        # Here, it finds the position of blank (0)
        zero = state.index(0)

        # Try every possible position where blank can move
        for move in moves[zero]:

            # list() converts the tuple into a list
            # Lists can be modified
            new_state = list(state)

            # Swap blank with the neighbouring tile
            new_state[zero], new_state[move] = \
                new_state[move], new_state[zero]

            # tuple() converts the list back to a tuple
            # Tuples can be stored in a set
            new_state = tuple(new_state)

            # Check whether this state has already been visited
            if new_state not in visited:

                # add() inserts the new state into the set
                visited.add(new_state)

                # append() adds the new state to the end of the queue
                # path + [state] stores the path followed so far
                queue.append((new_state, path + [state]))

    # Return None if no solution is found
    return None


# Initial puzzle state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


# Call bfs() function and store the returned solution
solution = bfs(start)


# Check whether a solution was found
if solution:

    # len() returns the number of states in the solution
    # Subtract 1 because the first state is the starting state
    print("Solution found in", len(solution) - 1, "moves:\n")

    # Display every state in the solution
    for step in solution:

        # Display first row
        print(step[0:3])

        # Display second row
        print(step[3:6])

        # Display third row
        print(step[6:9])

        # Print blank line between puzzle states
        print()

else:

    # Display message when no solution is found
    print("No solution found")

'''
| Method / Function | Work                                            |
| ----------------- | ----------------------------------------------- |
| `deque()`         | Creates a double-ended queue                    |
| `popleft()`       | Removes and returns the first item from a deque |
| `set()`           | Creates a set for storing unique values         |
| `index()`         | Returns the position of a specified value       |
| `list()`          | Converts a sequence into a list                 |
| `tuple()`         | Converts a sequence into a tuple                |
| `add()`           | Adds an item to a set                           |
| `append()`        | Adds an item to the end of a list/deque         |
| `len()`           | Returns the number of items                     |
| `print()`         | Displays output                                 |

'''



'''
# We're bringing in a tool called deque. Think of it as a list that's built to be
# fast whenever we keep adding or removing things from the front, which is exactly
# what our search is about to do, over and over again.
from collections import deque
# This is what a solved puzzle looks like - the exact arrangement we're aiming for.
# It's really just our 3x3 grid written out as 9 numbers in a row, and that 0 isn't
# a real tile at all - it's just standing in for the empty space.
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
# Before we even start solving anything, let's map out the grid. We'll number every
# square from 0 to 8, going left to right, top to bottom. Then for each square, we
# write down which squares sit right next to it, since that's exactly where the
# blank tile is allowed to slide. A corner only touches two squares, but the middle
# one touches four - we're working all of this out just once, up front, so the rest
# of the code never has to think about the grid's shape again.
moves = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
}
# Here's where the real work happens. This function takes one puzzle arrangement,
# called start, and tries to find a path from it all the way to the goal.

def bfs(start):
    # We're keeping two things close at hand while we search: a queue, which holds
    # every arrangement we still need to check, and a visited set, which remembers
    # every arrangement we've already looked at, so we never waste time on the same
    # one twice.

    queue = deque([(start, [])])
    visited = set([start])

    # We'll keep going for as long as there's still something waiting in the queue.

    while queue:
        # Each time through, we grab whatever's been sitting longest at the front of
        # the queue - that's what popleft does for us. state is the puzzle we're
        # looking at right now, and path is the whole trail of moves that got us here.
        state, path = queue.popleft()
        # Let's check - is this the exact puzzle we've been trying to reach? If it
        # is, we're done, and we can hand back the complete path right away, start
        # to finish.
        if state == goal:
            return path + [state]
        # Before we can make a move, we first need to know exactly where the blank
        # tile is sitting right now.
        zero = state.index(0)
        # Now let's try sliding the blank tile into every spot it's allowed to
        # reach from here.
        for move in moves[zero]:
            # We copy the puzzle as a list first, since tuples can't be changed
            # directly once they're created.
            new_state = list(state)
            # And here's the actual slide - we simply swap the blank tile with
            # whichever neighbour we're considering.
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            # Then we turn it back into a tuple, because a tuple is the only kind
            # of thing we're allowed to store inside our visited set.
            new_state = tuple(new_state)
            # If we've truly never seen this exact arrangement before, we mark it
            # as seen right away, and add it to the back of the queue so we get to
            # it later. If we've already seen it, there's nothing new to learn
            # here, so we just move on.
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    # If we ever run out of things in the queue without ever finding the goal,
    # that tells us this puzzle simply can't be solved from where we started.
    return None

# And here's the actual puzzle we want to solve - a little scrambled compared to
# the goal, but not too far off from it.
start = (1, 2, 3,
        4, 0, 6,
        7, 5, 8)

# Let's run the search now and see what comes back - either a full solution, or
# nothing at all, if the puzzle turns out to be unsolvable.
solution = bfs(start)
if solution:

    # If we did find a solution, let's first say how many moves it took.
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        # And then print out every step along the way as a proper 3x3 grid, so
        # it actually looks like the puzzle instead of just a row of numbers.
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print() # just a blank line here, to leave a little space between steps
else:
    print("No solution found")
'''

