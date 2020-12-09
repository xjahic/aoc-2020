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


def run_instructions(instructions: list, index_to_accumulator: dict, visited: list, accumulator: int, next_index: int):
    instructions_length = len(instructions)

    should_continue = True
    while should_continue:

        if next_index == instructions_length - 1:
            should_continue = False
            # Process last instruction and then finish
            (_, accumulator_addition) = process_instruction(instructions[next_index])
            accumulator += accumulator_addition

        elif next_index in visited:

            index_before_corrupt_instruction = visited[visited.index(next_index)]
            accumulator = index_to_accumulator[index_before_corrupt_instruction]
            visited.remove(next_index)

            (instruction, instruction_value) = instructions[next_index]
            if instruction == "nop":
                instructions[next_index] = ("jmp", instruction_value)
                return run_instructions(instructions, index_to_accumulator, visited, accumulator, next_index)
            elif instruction == "jmp":
                instructions[next_index] = ("nop", instruction_value)
                return run_instructions(instructions, index_to_accumulator, visited, accumulator, next_index)

        else:
            last_index = next_index
            visited.append(last_index)
            index_to_accumulator[last_index] = accumulator

            (index_change, accumulator_addition) = process_instruction(instructions[next_index])
            accumulator += accumulator_addition
            next_index = get_next_index(instructions_length, last_index, index_change)

    return accumulator


def read_instructions():
    instructions = []
    with open("input.txt") as f:
        for line in f:
            (key, v) = line.rstrip().split(" ")
            instructions.append((key, v))  # i.e 'nop', +0
    return instructions


print(run_instructions(read_instructions(), {}, [], 0, 0))  # Part 2
