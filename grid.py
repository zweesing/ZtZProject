from pathfinder import Pathfinder


gatesfilepath = "gates_and_netlists/print_0.csv"


def read_gates(path):
    """summary

    Args:
        path (string): path to csv file containing the gate positions

    Returns:
        dictionary, maxcoord: the dictioinary with the gate name and coordinates, and the max coordinate to determine grid size
    """
    gatesdict = {}
    max_coord = 0

    with open(gatesfilepath) as gatesfile:
        header = gatesfile.readline()
        lines = gatesfile.readlines()

        for line in lines:
            line = line.strip().split(",")
            gatesdict[line[0]] = (int(line[1]), int(line[2]))
            if int(line[1]) > max_coord:
                max_coord = int(line[1])

            if int(line[2]) > max_coord:
                max_coord = int(line[2])

    return gatesdict, max_coord


# now only squares. need to test x and y seperatly to also make rectangles if needed.


class Grid:
    def __init__(self, column, row, gates):
        self.column = column
        self.row = row
        self.board = []
        self.gates_dict = gates
        self.make_board()

    def make_board(self):
        # Function makes a board based on the column and row input of the user
        for row in range(self.row):
            self.board.append([])
            for width in range(self.column):
                self.board[row].append("0")

        # add gates
        for gate in self.gates_dict:
            self.place_gate(self.gates_dict[gate])

    def get_board(self):
        return self.board

    def place_gate(self, coords):
        # Places a gate at the coordinates given by the user
        column, row = coords
        self.board[column][row] = "X"

    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])


# Make a dictionary at the end were net list(route) is linked to the actual found route.


if __name__ == "__main__":

    # g = Grid(10, 10)
    # g.get_board()
    # print(g)
    # print()
    # g.place_gate(4, 4)
    # print(g)
    gatesfilepath = "gates_and_netlists/print_0.csv"
    dict, max_coord = read_gates(gatesfilepath)
    size = max_coord + 1
    p = Grid(size, size, dict)
    print(p)

    b = p.get_board()
    g = Pathfinder((0, 0), (4, 4), b)
    print()
    route, wire_count, board = g.find()
    print(g)
    print(route)
