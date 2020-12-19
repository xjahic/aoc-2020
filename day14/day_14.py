memory = {}


def process_number(mask, index, value):
    result = []
    for i in range(36):
        if mask[i] == "X":
            result.append(value[i])
        else:
            result.append(mask[i])
    memory[index] = int("".join(result), 2)


with open("input.txt") as f:
    current_mask = ""
    for line in f:
        if line.startswith("mask"):
            current_mask = line[7:-1]
        else:
            memory_index = line[4:line.find("]")]
            value = bin(int(line[line.find("]") + 3:]))[2:]
            process_number(current_mask, memory_index, str(value).rjust(36, "0"))

print(sum(memory.values()))
