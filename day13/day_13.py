
def get_data():
    with open("input.txt") as f:
        lines = f.readlines()
        earliest_estimate = int(lines[0].rstrip())
        buses_timestamps = [int(time) for time in lines[1].split(",") if time != "x"]
        return earliest_estimate, buses_timestamps


timestamp, buses = get_data()

earliest_bus, minutes = buses[0], buses[0]
for bus in buses:
    time = bus
    while timestamp > time:
        time += bus
    if time - timestamp < minutes:
        earliest_bus = bus
        minutes = time - timestamp

print(earliest_bus * minutes)

