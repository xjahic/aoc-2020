def binary_partitioning(left, right, text, lower_sign, upper_sign):
    for index in range(len(text)):
        mid = 1 + (right - left) // 2
        if text[index] == lower_sign:
            right = right - mid
        elif text[index] == upper_sign:
            left = left + mid
    return left


def get_seat_id(boarding_pass):
    row = binary_partitioning(0, 127, boarding_pass[0:7], "F", "B")
    column = binary_partitioning(0, 7, boarding_pass[7:10], "L", "R")
    return row * 8 + column


# read seats
seats = [get_seat_id(line.rstrip()) for line in open("input.txt")]

print(max(seats))  # part 1

seats.sort()  # sort seats

# part 2 - imperative
previous = seats[0]
for i in range(1, len(seats)):
    if seats[i] - previous != 1:
        print(seats[i] - 1)  # part 2
        break
    else:
        previous = seats[i]

# part 2 - declarative
print(next(seats[i] - 1 for i in range(1, len(seats)) if seats[i] - seats[i - 1] != 1))
