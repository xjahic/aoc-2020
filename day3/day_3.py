from functools import reduce

LINE_LENGTH_STRIPPED = 31

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
slope_to_result = {}
lines_hopped = 1

with open("input.txt") as f:
    next(f)  # skip first line
    for line in f:
        for i in range(5):
            down_steps = slopes[i][1]
            if lines_hopped % down_steps != 0:
                continue
            column = slopes[i][0] * int(lines_hopped / down_steps) % LINE_LENGTH_STRIPPED
            if line[column] == "#":
                slope_to_result[i] = slope_to_result.get(i, 0) + 1
        lines_hopped += 1

print(slope_to_result)

result = reduce((lambda x, y: x * y), slope_to_result.values())
print(result)