def main():
    f = open("input", "r")
    lines = f.read().split("\n")
    seats = []
    for line in lines:
        row = [i for i in range(128)]
        col = [i for i in range(8)]
        for char in line:
            if char == "F":
                row = row[: len(row) // 2]
            elif char == "B":
                row = row[len(row) // 2 :]
            elif char == "L":
                col = col[: len(col) // 2]
            elif char == "R":
                col = col[len(col) // 2 :]
        seats.append((row[0], col[0], row[0] * 8 + col[0]))

    # part 1
    ids = [seat[2] for seat in seats]
    max_id = max(ids)
    print("Max id: ", max_id)

    # part 2
    seats = sorted(seats, key=lambda id: id[2])
    for i in range(48, len(seats)):
        if seats[i - 48][2] != i:
            print("My seat: ", seats[i - 1 - 48][2] + 1)
            break


if __name__ == "__main__":
    main()