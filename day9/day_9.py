import itertools

all_numbers = []
preamble_length = 25
preambles = []

# sum_possibilities is not a set because multiple numbers can produce the same sum so
# removing sum would wrongly remove possibilities
sum_possibilities = []

invalid_number_part1 = 0

with open("input.txt") as f:
    first_batch_done = False
    for line in f:
        number = int(line.rstrip())
        all_numbers.append(number)

        if first_batch_done:
            if number not in sum_possibilities:
                invalid_number_part1 = number
                break

            first_preamble = preambles[0]
            # remove possibilities from first preamble
            for to_remove in [num + first_preamble for num in preambles[1:]]:
                sum_possibilities.remove(to_remove)
            # remove first preamble
            preambles.remove(first_preamble)
            # add new possibilities
            sum_possibilities += ([preamble + number for preamble in preambles])
            # add new preamble
            preambles.append(number)

        else:
            preambles.append(number)
            if len(preambles) == preamble_length:
                first_batch_done = True
                sum_possibilities += ([perm[0] + perm[1] for perm in itertools.permutations(preambles, 2)])

print(invalid_number_part1)  # Part 1

contiguous_numbers = []
current_sum = 0
should_continue = True

for number in all_numbers:

    if not should_continue:
        break

    sum_with_next_number = current_sum + number
    contiguous_numbers.append(number)

    if sum_with_next_number == invalid_number_part1:  # Result by adding new number to existing numbers
        print(min(contiguous_numbers) + max(contiguous_numbers))  # Part 2
        break
    if sum_with_next_number < invalid_number_part1:
        current_sum = sum_with_next_number
    else:
        current_sum = sum_with_next_number
        while current_sum > invalid_number_part1:
            first_contiguous = contiguous_numbers[0]
            current_sum -= first_contiguous
            contiguous_numbers.remove(first_contiguous)
            # Result by removing old numbers in existing numbers (including new number)
            if current_sum == invalid_number_part1:
                print(min(contiguous_numbers) + max(contiguous_numbers))  # Part 2
                should_continue = False
                break
