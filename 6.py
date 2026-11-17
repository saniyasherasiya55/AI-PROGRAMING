import heapq

def heuristic(state, goal):

    distance = 0

    for i in range(9):

        if state[i] == 0:
            continue

        row1 = i // 3
        col1 = i % 3

        j = goal.index(state[i])

        row2 = j // 3
        col2 = j % 3

        distance = distance + abs(row1 - row2)
        distance = distance + abs(col1 - col2)

    return distance


def solve(start, goal):

    queue = []

    heapq.heappush(
        queue,
        (heuristic(start, goal), start)
    )

    visited = set()

    while queue:

        h, state = heapq.heappop(queue)

        print("State:", state, "Heuristic:", h)

        if state == goal:
            print("Goal Reached")
            return

        visited.add(state)

        zero = state.index(0)

        row = zero // 3
        col = zero % 3

        moves = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in moves:

            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_zero = new_row * 3 + new_col

                new_state = list(state)

                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:

                    value = heuristic(new_state, goal)

                    heapq.heappush(
                        queue,
                        (value, new_state)
                    )


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

solve(start, goal)
