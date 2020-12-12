def manhattan_distance():
    return abs(ship_directions["X"]) + abs(ship_directions["Y"])


waypoint_direction = {"X": 10, "Y": 1}
ship_directions = {"X": 0, "Y": 0}


def move_ship_relative_to_waypoint(val: int):
    ship_directions["X"] = ship_directions["X"] + waypoint_direction["X"] * val
    ship_directions["Y"] = ship_directions["Y"] + waypoint_direction["Y"] * val


with open("input.txt") as f:
    for line in f:
        action, value = line[0], int(line.rstrip()[1:])
        if action == "F":
            move_ship_relative_to_waypoint(value)
        elif action == "L":
            turns = int(value / 90)
            for i in range(turns):
                (x, y) = waypoint_direction["X"], waypoint_direction["Y"]
                waypoint_direction["X"] = -y
                waypoint_direction["Y"] = x
        elif action == "R":
            turns = int(value / 90)
            for i in range(turns):
                (x, y) = waypoint_direction["X"], waypoint_direction["Y"]
                waypoint_direction["X"] = y
                waypoint_direction["Y"] = -x
        else:
            if action == "N":
                waypoint_direction["Y"] = waypoint_direction.get("Y") + value
            elif action == "S":
                waypoint_direction["Y"] = waypoint_direction.get("Y") - value
            elif action == "E":
                waypoint_direction["X"] = waypoint_direction.get("X") + value
            elif action == "W":
                waypoint_direction["X"] = waypoint_direction.get("X") - value

print(manhattan_distance())
