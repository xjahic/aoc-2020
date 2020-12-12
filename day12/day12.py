def manhattan_distance():
    return abs(ship_directions["E"] - ship_directions["W"]) + abs(ship_directions["N"] - ship_directions["S"])


directions = "WNES"
ship_directions = {"E": 0, "W": 0, "N": 0, "S": 0}
facing = "E"

with open("input.txt") as f:
    for line in f:
        action, value = line[0], int(line.rstrip()[1:])
        if action == "F":
            ship_directions[facing] = ship_directions.get(facing) + value
        elif action == "L":
            turns = int(value / 90)
            facing = directions[(directions.index(facing) - turns) % 4]
        elif action == "R":
            turns = int(value / 90)
            facing = directions[(directions.index(facing) + turns) % 4]
        else:
            ship_directions[action] = ship_directions.get(action) + value

print(manhattan_distance())
