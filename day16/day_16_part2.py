from itertools import permutations

ranges_done = False
nearby_tickets_reading = False
my_ticket_reading = False

my_ticket = []
all_possible_numbers = set()
valid_ranges = []
nearby_tickets = []

index_position = 0

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            ranges_done = True

        elif not ranges_done:
            name = line[:line.find(":")]

            first_range = line[line.find(":") + 2:line.find("or ") - 1].split("-")
            valid_numbers = set(range(int(first_range[0]), int(first_range[1]) + 1))

            second_range = line[line.find("or ") + 3:line.find("\n")].split("-")
            valid_numbers.update(set(range(int(second_range[0]), int(second_range[1]) + 1)))

            all_possible_numbers.update(valid_numbers)
            valid_ranges.append({name: valid_numbers})
            index_position += 1

        elif my_ticket_reading:
            my_ticket = [int(number) for number in line.rstrip().split(",")]
            my_ticket_reading = False

        elif line.startswith("your ticket"):
            my_ticket_reading = True

        elif line.startswith("nearby tickets"):
            nearby_tickets_reading = True

        elif nearby_tickets_reading:
            nearby_tickets_line = [int(number) for number in line.rstrip().split(",")]
            if len([ticket for ticket in nearby_tickets_line if ticket not in all_possible_numbers]) == 0:
                nearby_tickets.append(nearby_tickets_line)

print(valid_ranges)
print(nearby_tickets)

result_permutation = []
for index_looking in range(len(valid_ranges)):
    for i in range(len(valid_ranges)):
        found_index_looking = True
        for ticket in nearby_tickets:
            if ticket[index_looking] not in list((valid_ranges[i].values()))[0]:
                found_index_looking = False
                break
        if found_index_looking and i not in result_permutation:
            result_permutation.append(i)
            found_me = True
            break

print("found permutation", result_permutation)

final_result = 1
i = 0
for valid_range in valid_ranges:
    for key in valid_range:
        if key.startswith("departure"):
            final_result *= my_ticket[i]
    i += 1
print(final_result)


# keys_permutations = list(permutations(valid_ranges.keys()))
# result_permutation = []
#
# for key_permutation in keys_permutations:
#     should_continue_checking_tickets = True
#     for ticket in nearby_tickets:
#         if not should_continue_checking_tickets:
#             break
#         for i in range(0, len(ticket)):
#             if ticket[i] not in valid_ranges[key_permutation[i]]:
#                 should_continue_checking_tickets = False
#                 break
#     if should_continue_checking_tickets:
#         print("Found permutation", key_permutation)
#         result_permutation = key_permutation
#         break
