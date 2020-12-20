puzzle = "11,0,1,10,5,19"

numbers = [int(number) for number in puzzle.split(",")]

number_to_indexes = {}
i = 1
for number in numbers:
    number_to_indexes[number] = [i]
    i += 1

last_number_spoken = numbers[-1]

for i in range(len(numbers), 2020):
    if len(number_to_indexes[last_number_spoken]) == 1:
        next_number = 0
        last_number_spoken = next_number
        number_to_indexes[last_number_spoken] = number_to_indexes.get(last_number_spoken, []) + [i + 1]
    else:
        # first time
        indexes_of_previous_number = number_to_indexes[last_number_spoken]
        next_number = indexes_of_previous_number[-1] - indexes_of_previous_number[-2]
        last_number_spoken = next_number
        number_to_indexes[last_number_spoken] = number_to_indexes.get(last_number_spoken, []) + [i + 1]


print(last_number_spoken)
