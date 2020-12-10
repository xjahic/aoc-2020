adapters = [0]
adapters += [int(adapter.rstrip()) for adapter in open("input.txt")]
adapters.sort()
adapters.append(adapters[-1] + 3)

differences = {}
groups = []
current_group = []
previous_adapter = adapters[0]
for i in range(1, len(adapters)):
    adapter = adapters[i]
    diff = adapter - previous_adapter
    differences[diff] = differences.get(diff, 0) + 1
    if diff == 1:
        current_group.append(adapter)
    elif diff == 3:
        if previous_adapter in current_group:
            current_group.remove(previous_adapter)
        if len(current_group) > 0:
            groups.append(current_group)
        current_group = []
    previous_adapter = adapter

print(differences[1] * differences[3])  # part 1

result = 1
for group in groups:
    group_size = len(group)
    if group_size < 3:
        result *= 2 ** group_size
    elif group_size == 3:
        result *= 2 ** group_size - 1
print(result)  # part 2

#  How is part 2 solved?
#  i.e. adapters: [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
#  Get group of numbers which do not have to be necessarily present in the adapters
#  [[1, 2, 3], [8, 9, 10], [18, 19], [24], [32, 33, 34], [46, 47, 48]]
#  When group has 1 or 2 adapters, none of them need to be in the final adapters - so thats 4 possiblities (2^2 - none, only first, only second, both)
#  And when there are 3 items in the group - at least 1 has to be present, so that is 2^3 - 1 possibilities
#  Final number of possibilities depends on these groups, we multiply each group possibility
#  There are no groups (in this input!) which length was longer than 3
