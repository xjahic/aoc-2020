import itertools

fhand = open("input.txt")
numbers = [int(line.rstrip()) for line in fhand]
fhand.close()

########################## IMPERATIVE PART 1 #############################
result_part1 = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            result_part1 = numbers[i] * numbers[j]
            break
print(result_part1)

########################## IMPERATIVE PART 2 #############################

result_part2 = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                result_part2 = numbers[i] * numbers[j] * numbers[k]
                break
print(result_part2)


########################## DECLARATIVE PART 1 #############################

result_permutation = next(perm for perm in itertools.permutations(numbers, 2) if perm[0] + perm[1] == 2020)
print(result_permutation[0] * result_permutation[1])

########################## DECLARATIVE PART 2 #############################

result_permutation = next(perm for perm in itertools.permutations(numbers, 3) if perm[0] + perm[1] + perm[2] == 2020)
print(result_permutation[0] * result_permutation[1] * result_permutation[2])