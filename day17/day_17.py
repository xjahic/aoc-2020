import pprint

ACTIVE = "#"
INACTIVE = "."


def get_initial_state():
    with open("input.txt") as f:
        initial_state = {0: [[0 for c in range(3)] for r in range(3)]}
        for row, line in enumerate(f):  # row is 0, 1, 2
            for column, c in enumerate(line.rstrip()):  # column is 0, 1, 2
                initial_state[0][row][column] = c == ACTIVE
        return initial_state


def process(state: {}, cycles: int):
    new_state = {}
    print("initial_state", state)
    for z in range(-1, 2, 1):  # cycle 1
        # tu vlozit prazdne ak neexistuje index
        if z not in new_state:
            new_state[z] = [[False for c in range(3)] for r in range(3)]

        #  ukladam new state podla initial state
        #  teraz pozeram na aktualne z tak, ze idem -1, z, z + 1
        for row in range(0, 3):
            for column in range(0, 3):
                # pre kazdy znak ceknem ostatnych 26 znakov

                count_active = 0
                # cycle neighbours
                for cycle_z in range(z - 1, z + 2, 1):
                    for r in range(row - 1, row + 2, 1):
                        for c in range(column - 1, column + 2, 1):
                            if cycle_z == z and r == row and column == c:
                                continue  # toto je ten isty znak ktory idem menit
                            try:
                                if state[cycle_z][r][c]:
                                    count_active += 1
                            except KeyError:
                                # print("index error pri cycle neighbours")
                                break
                            except IndexError:
                                # print("")
                                break
                try:
                    if state[z][row][column]:
                        print("ACTIVE and count = ", count_active)
                        if count_active == 2 or count_active == 3:
                            new_state[z][row][column] = True
                        else:
                            new_state[z][row][column] = False
                    else:
                        print("INACTIVE and count = ", count_active)
                        if count_active == 3:
                            new_state[z][row][column] = True
                except KeyError:
                    # state[z] wasn't found, so let it be like it was inactive
                    if count_active == 3:
                        new_state[z][row][column] = True

    print(new_state)


process(get_initial_state(), 1)
