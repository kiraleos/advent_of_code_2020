def main():
    f = open("input", "r")
    lines = [line.strip() for line in f.readlines()]
    num_valid_passwords_part_1 = 0
    num_valid_passwords_part_2 = 0
    for line in lines:
        policy = line.split(":")[0]
        password = line.split(":")[1].strip()
        min_times = int(policy.split("-")[0])
        max_times = int(policy.split("-")[1].split(" ")[0])
        char = policy.split("-")[-1][-1]

        # part 1

        occurences = 0
        for c in password:
            if c == char:
                occurences += 1

        if occurences >= min_times and occurences <= max_times:
            num_valid_passwords_part_1 += 1

        # part 2
        pos_1 = min_times
        pos_2 = max_times
        if bool(password[pos_1 - 1] == char) != bool(password[pos_2 - 1] == char):
            num_valid_passwords_part_2 += 1

    print("Part 1: ", num_valid_passwords_part_1)
    print("Part 2: ", num_valid_passwords_part_2)


if __name__ == "__main__":
    main()