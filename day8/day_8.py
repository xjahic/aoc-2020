def get_next_index(instructions_length, last_index, index_change):
    next_index = (last_index + index_change) % instructions_length
    return next_index


def process_instruction(instruction: tuple):
    (instruction, instruction_value) = instruction
    accumulator = 0
    index_change = 0

    if instruction == "nop":
        index_change = 1
    elif instruction == "acc":
        accumulator += int(instruction_value)
        index_change = 1
    elif instruction == "jmp":
        index_change = int(instruction_value)

    return index_change, accumulator


def run_instructions(instructions: list):
    instructions_length = len(instructions)

    (index_change, accumulator) = process_instruction(instructions[0])
    visited_indexes = [0]
    last_index = 0

    should_continue = True
    while should_continue:
        next_index = get_next_index(instructions_length, last_index, index_change)
        if next_index in visited_indexes:
            should_continue = False
        else:
            (index_change, accumulator_addition) = process_instruction(instructions[next_index])
            last_index = next_index
            accumulator += accumulator_addition
            visited_indexes.append(next_index)

    return accumulator


def read_instructions():
    instructions = []
    with open("input.txt") as f:
        for line in f:
            (key, v) = line.rstrip().split(" ")
            instructions.append((key, v))  # i.e 'nop', +0
    return instructions


print(run_instructions(read_instructions()))  # Part 1
