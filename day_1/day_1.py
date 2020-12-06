def main():
    f = open("input", "r")
    nums = [int(line.strip()) for line in f.readlines()]
    sums = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                sums.append((nums[i] + nums[j] + nums[k], i, j, k))

    for sum in sums:
        if sum[0] == 2020:
            print(nums[sum[1]] * nums[sum[2]] * nums[sum[3]])


if __name__ == "__main__":
    main()