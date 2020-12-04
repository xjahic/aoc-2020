import re

################################# PART 1 #################################

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

valid_passports = 0
current_passport_fields = []

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            # check current passport
            if all(required in current_passport_fields for required in required_fields): valid_passports += 1
            current_passport_fields.clear()
        else:
            # add fields to current passport
            current_passport_fields += ([field[:field.index(":")] for field in line.rstrip().split(" ")])

# for the last line
if all(required in current_passport_fields for required in required_fields): valid_passports += 1

print(valid_passports)

################################# PART 2 #################################

required_fields = {"byr": "^(19[2-9][0-9]|200[0-2])$",
                   "iyr": "^20(1[0-9]|20)$",
                   "eyr": "^20(2[0-9]|30)$",
                   "hgt": "^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$",
                   "hcl": "^#[0-9a-f]{6}$",
                   "ecl": "^(amb|blu|brn|gry|grn|hzl|oth)$",
                   "pid": "^[0-9]{9}$"
                   }

valid_passports = 0
current_passport_fields = {}


def is_passport_valid(passport_fields: dict):
    for required, regex in required_fields.items():
        if required not in passport_fields or not re.search(regex, passport_fields[required]):
            return False
    return True


with open("input.txt") as f:
    for line in f:
        if line == "\n":
            # check current passport
            if is_passport_valid(current_passport_fields): valid_passports += 1
            current_passport_fields.clear()
        else:
            # add fields to current passport
            for raw_field in line.rstrip().split(" "):
                (field, value) = raw_field.split(":")
                current_passport_fields[field] = value

# for the last line
if is_passport_valid(current_passport_fields): valid_passports += 1

print(valid_passports)
