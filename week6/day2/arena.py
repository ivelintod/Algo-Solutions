class ChessFloor:

    def __init__(self, floor):
        self.floor = floor

    def minimumChanges(self, floor):
        #colours = set()
        max_el = None
        max_colour = None
        second_max_el = None
        second_max_colour = None
        changes = 0
        colours = {}
        for row in range(len(floor)):
            for tile in range(len(floor)):
                #if floor[row][tile] == floor[row][tile + 1]:
                #    count_consecutive += 1
                #colours.add(floor[row][tile])
                colours[floor[row][tile]] = 0

        for row in range(len(floor)):
            for tile in range(len(floor)):
                colours[floor[row][tile]] += 1
                max_el = colours[floor[row][tile]]
                second_max_el = colours[floor[row][tile]]

        for row in range(len(floor)):
            for tile in range(len(floor)):
                if colours[floor[row][tile]] > max_el:
                    max_el = colours[floor[row][tile]]
                    max_colour = floor[row][tile]

        for row in range(len(floor)):
            for tile in range(len(floor)):
                if colours[floor[row][tile]] > second_max_el and floor[row][tile] != max_colour:
                    second_max_el = colours[floor[row][tile]]
                    second_max_colour = floor[row][tile]

        most_common = (max_colour, second_max_colour)


        for row in floor:
            if most_common[0] and most_common[1] not in row:
                changes += len(floor)

        start = floor[0][0]
        for row in range(len(floor)):
            for tile in range(len(floor)):
                if floor[row][tile] != start
                    break





def main():
    c = ChessFloor(("helloand",
                    "welcomet",
                    "osingler",
                    "oundmatc",
                    "hsixhund",
                    "redandsi",
                    "xtythree",
                    "goodluck"))
    c.minimumChanges(c.floor)

if __name__ == '__main__':
    main()
