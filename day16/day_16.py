ranges_done = False
nearby_tickets_reading = False
possible_numbers = set()
not_in_range = []
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            ranges_done = True
        elif not ranges_done:
            first_range = line[line.find(":") + 2:line.find("or ") - 1].split("-")
            possible_numbers.update(set(range(int(first_range[0]), int(first_range[1]) + 1)))

            second_range = line[line.find("or ") + 3:line.find("\n")].split("-")
            possible_numbers.update(set(range(int(second_range[0]), int(second_range[1]) + 1)))
        elif line.startswith("nearby tickets"):
            nearby_tickets_reading = True
        elif nearby_tickets_reading:
            nearby_tickets = [int(number) for number in line.rstrip().split(",")]
            not_in_range += [ticket for ticket in nearby_tickets if ticket not in possible_numbers]

print(sum(not_in_range))
