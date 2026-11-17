def water_jug_dfs():

    jug1 = 4
    jug2 = 3
    goal = 2

    stack = [(0, 0)]

    visited = set()

    while stack:

        a, b = stack.pop()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        print(a, b)

        if a == goal:
            print("Goal Reached")
            return

        states = []

        # Fill jug 1
        states.append((jug1, b))

        # Fill jug 2
        states.append((a, jug2))

        # Empty jug 1
        states.append((0, b))

        # Empty jug 2
        states.append((a, 0))

        # Pour jug 1 into jug 2
        amount = min(a, jug2 - b)
        states.append((a - amount, b + amount))

        # Pour jug 2 into jug 1
        amount = min(b, jug1 - a)
        states.append((a + amount, b - amount))

        for state in states:

            if state not in visited:
                stack.append(state)


water_jug_dfs()
