import itertools

memory = {}


def process_number(mask, index, value):
    # value is number which will be saved in each memory index
    # index is 36 bit number
    result = []
    memory_indexes = []
    for i in range(36):
        if mask[i] == "0":
            result.append(index[i])
        else:
            result.append(mask[i])

    result_joined = "".join(result)

    floating_variations = list(itertools.product([0, 1], repeat=result_joined.count("X")))
    for variation in floating_variations:
        tmp_result = result_joined
        for bit in variation:
            tmp_result = tmp_result.replace("X", str(bit), 1)
        memory_indexes.append(tmp_result)

    for m_index in memory_indexes:
        memory[int(memory_index, 2)] = value


with open("input.txt") as f:
    current_mask = ""
    for line in f:
        if line.startswith("mask"):
            current_mask = line[7:-1]
        else:
            memory_index = bin(int(line[4:line.find("]")]))[2:]
            value_to_save = line[line.find("]") + 3:]
            process_number(current_mask, str(memory_index).rjust(36, "0"), int(value_to_save))

print(sum(memory.values()))