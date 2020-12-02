fhand = open("input.txt")

count_valid_part1 = 0
count_valid_part2 = 0

for line in fhand:
    split_line = line.rstrip().split(" ")
    (valid_range, current_char, password) = (split_line[0].split("-"), split_line[1][0], split_line[2])

    if int(valid_range[0]) <= password.count(current_char) <= int(valid_range[1]):
        count_valid_part1 += 1

    is_at_position_1 = current_char == password[int(valid_range[0]) - 1]
    is_at_position_2 = current_char == password[int(valid_range[1]) - 1]
    if is_at_position_1 != is_at_position_2:
        count_valid_part2 += 1

print(count_valid_part1)
print(count_valid_part2)

fhand.close()
