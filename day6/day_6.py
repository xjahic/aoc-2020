######################### PART 1 ###########################

total_result = 0
current_answers = set()

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            total_result += len(current_answers)
            current_answers.clear()
        else:
            for c in line.rstrip():
                current_answers.add(c)

total_result += len(current_answers)

print(total_result)

######################### PART 2 ###########################


total_result = 0
correct_answers = []

with open("input.txt") as f:
    for line in f:
        if line == "\n":
            total_result += len(set.intersection(*correct_answers))
            correct_answers.clear()
        else:
            correct_answers.append(set([c for c in line.rstrip()]))

total_result += len(set.intersection(*correct_answers))

print(total_result)
