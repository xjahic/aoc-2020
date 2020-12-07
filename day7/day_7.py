def total_bags(start, result):
    total = result
    inner_routes = [(key[0], key[1]) for key in routes[start]]
    for k, v in inner_routes:
        total += result * total_bags(k, int(v))
    return total


def find_paths(start, path: list):
    path.append(start)
    if start == shiny_gold:
        return path

    found_paths = []
    inner_routes = [key[0] for key in routes[start]]

    for inner_route in inner_routes:
        if inner_route not in path:
            [found_paths.append(found) for found in find_paths(inner_route, path)]

    return found_paths


def content_to_tuple(bag: str):
    # from 2 muted yellow bags makes (muted yellow, 2)
    return bag[bag.find(" ") + 1:bag.find("bag") - 1], bag[:bag.find(" ")]


routes = {}
with open("input.txt") as f:
    for line in f:
        bags_start_index = line.find("bags")
        key_bag = line[:bags_start_index - 1]
        contents = line.rstrip()[bags_start_index + 13:-1].split(", ")
        routes[key_bag] = [content_to_tuple(bag) for bag in contents if not bag.startswith("n")]

shiny_gold = "shiny gold"
possible_routes = [find_paths(route, [route]) for route in routes if route != shiny_gold]

print(len([route for route in possible_routes if len(route) > 0]))  # Part 1
print(total_bags(shiny_gold, 1) - 1)  # Part 2
