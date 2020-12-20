puzzle = "11,0,1,10,5,19"

numbers = [int(number) for number in puzzle.split(",")]

number_to_indexes = {}
i = 1
for number in numbers:
    number_to_indexes[number] = {"first_index": i, "second_index": -1}
    i += 1

last_number_spoken = numbers[-1]

for i in range(len(numbers), 2020):

    next_number = -1
    if number_to_indexes[last_number_spoken]["second_index"] == -1:
        next_number = 0
    else:
        indexes = number_to_indexes[last_number_spoken]
        next_number = indexes["second_index"] - indexes["first_index"]

    if next_number not in number_to_indexes:
        number_to_indexes[next_number] = {"first_index": i + 1, "second_index": -1}

    elif number_to_indexes[next_number]["second_index"] != -1:
        number_to_indexes[next_number]["first_index"] = number_to_indexes[next_number]["second_index"]
        number_to_indexes[next_number]["second_index"] = i + 1
    else:
        number_to_indexes[next_number]["second_index"] = i + 1

    last_number_spoken = next_number

print(last_number_spoken)
