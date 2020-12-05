def main():
    f = open("input", "r")
    map = [char for char in f.read() if char != "\n"]
    map = [map[i : i + 31] for i in range(0, len(map), 31)]

    # part 1
    num_trees = 0
    i, j = 0, 0
    while i < len(map):
        if map[i][j] == "#":
            num_trees += 1

        i += 1
        j = (j + 3) % 31

    print("Part 1: ", num_trees)

    # part 2
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    num_trees = {slope: 0 for slope in slopes}
    for slope in slopes:
        i, j = 0, 0
        while i < len(map):
            if map[i][j] == "#":
                num_trees[slope] += 1

            i += slope[0]
            j = (j + slope[1]) % 31

    prod = 1
    for val in num_trees.values():
        print(val)
        prod *= val
    print("Part 2: ", prod)


if __name__ == "__main__":
    main()