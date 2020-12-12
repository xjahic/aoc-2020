def manhattan_distance():
    return abs(ship_directions["E"] - ship_directions["W"]) + abs(ship_directions["N"] - ship_directions["S"])


directions = "WNES"
waypoint_direction = {"E": 10, "W": 0, "N": 1, "S": 0}
ship_directions = {"E": 0, "W": 0, "N": 0, "S": 0}


def move_ship_relative_to_waypoint(val: int):
    for k, v in waypoint_direction.items():
        if v > 0:
            ship_directions[k] = ship_directions.get(k) + v * val


with open("input.txt") as f:
    for line in f:
        action, value = line[0], int(line.rstrip()[1:])
        if action == "F":
            move_ship_relative_to_waypoint(value)
        elif action == "L":
            turns = int(value / 90)
            rotated_directions = directions[-turns:] + directions[:-turns]  # rotation
            new_waypoint_directions = {"E": 0, "W": 0, "N": 0, "S": 0}
            for i in range(len(directions)):
                waypoint_direction[rotated_directions[i]] = waypoint_direction[directions[i]]
            waypoint_direction = new_waypoint_directions
        elif action == "R":
            turns = int(value / 90)
            rotated_directions = directions[turns:] + directions[:turns]  # rotation
            new_waypoint_directions = {"E": 0, "W": 0, "N": 0, "S": 0}
            for i in range(len(directions)):
                new_waypoint_directions[rotated_directions[i]] = waypoint_direction[directions[i]]
            waypoint_direction = new_waypoint_directions
        else:
            waypoint_direction[action] = waypoint_direction.get(action) + value

print(manhattan_distance())
