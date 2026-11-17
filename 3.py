def dfs(start, goal):

    stack = [(start, [])]

    visited = set()

    while stack:

        state, path = stack.pop()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

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
                    stack.append((new_state, path + [state]))

    return None


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

solution = dfs(start, goal)

print("DFS Solution")

for state in solution:

    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
    print()
