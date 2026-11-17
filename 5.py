def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:

        print("Move disk 1 from", source, "to", destination)

        return

    tower_of_hanoi(
        n - 1,
        source,
        destination,
        auxiliary
    )

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(
        n - 1,
        auxiliary,
        source,
        destination
    )


n = 3

print("Tower of Hanoi")

tower_of_hanoi(n, 'A', 'B', 'C')
