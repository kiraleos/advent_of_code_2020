import json
import re


def main():
    f = open("input", "r")
    string = f.read()
    lines = string.splitlines(False)

    passports = []
    temp = ""
    for line in lines:
        if line != "":
            temp += line + " "
        else:
            passports.append(temp)
            temp = ""

    passports = [passport.split(" ") for passport in passports]
    for passport in passports:
        passport = passport.pop()

    passports_dict = {}
    i = 1
    for passport in passports:
        passports_dict[i] = {}
        for elem in passport:
            key, value = elem.split(":")
            passports_dict[i][key] = value
        i += 1

    valid_ctr = 0
    for passport in passports_dict.values():
        if (
            "byr" in passport
            and "iyr" in passport
            and "eyr" in passport
            and "hgt" in passport
            and "hcl" in passport
            and "ecl" in passport
            and "pid" in passport
        ):
            sub_ctr = 0
            byr = passport["byr"]
            if len(byr) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
                sub_ctr += 1
            iyr = passport["iyr"]
            if len(iyr) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
                sub_ctr += 1
            eyr = passport["eyr"]
            if len(eyr) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
                sub_ctr += 1
            hgt = passport["hgt"]
            regex = re.compile("[0-9].+(cm|in)")
            if regex.match(hgt):
                if hgt[-2:] == "cm":
                    if int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193:
                        sub_ctr += 1
                elif hgt[-2:] == "in":
                    if int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76:
                        sub_ctr += 1
            hcl = passport["hcl"]
            regex = re.compile("#[0-9a-f]{6}")
            if regex.match(hcl):
                sub_ctr += 1
            ecl = passport["ecl"]
            if (
                ecl == "amb"
                or ecl == "blu"
                or ecl == "brn"
                or ecl == "gry"
                or ecl == "grn"
                or ecl == "hzl"
                or ecl == "oth"
            ):
                sub_ctr += 1
            pid = passport["pid"]
            regex = re.compile("^[0-9]{9}$")
            if regex.match(pid):
                print(pid)
                sub_ctr += 1
            if sub_ctr == 7:
                valid_ctr += 1

    # print(json.dumps(passports_dict, indent=4))
    print("Valid passports: ", valid_ctr)


if __name__ == "__main__":
    main()