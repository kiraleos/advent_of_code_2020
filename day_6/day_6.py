def main():
    f = open("input", "r")
    lines = f.readlines()
    groups = []
    group = []
    for line in lines:
        if line != "\n":
            group.append(line.strip())
        else:
            groups.append(group)
            group = []

    s1 = 0
    s2 = 0
    for group in groups:
        answers = []
        for answer in group:
            answers.append(set(answer))
        s1 += len(set.union(*answers))
        s2 += len(set.intersection(*answers))
    print(s1)
    print(s2)


if __name__ == "__main__":
    main()