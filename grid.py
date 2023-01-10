from pathfinder import Pathfinder

gatesdict = {}
gatesfilepath = "gates_and_netlists/print_0.csv"
with open(gatesfilepath) as gatesfile:
    header = gatesfile.readline()
    lines = gatesfile.readlines()

    for line in lines:
        line = line.strip().split(",")
        gatesdict[line[0]] = (int(line[1]), int(line[2]))


class Grid:
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.board = []
        self.make_board()

    def make_board(self):
        # Function makes a board based on the column and row input of the user
        for row in range(self.row):
            self.board.append([])
            for width in range(self.column):
                self.board[row].append("0")

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
    p = Grid(7, 7)

    for gate in gatesdict:
        print(gatesdict[gate])
        p.place_gate(gatesdict[gate])

    b = p.get_board()
    g = Pathfinder((0, 0), (4, 4), b)
    print(p)
    print()
    route, wire_count, board = g.find()
    print(g)
    print(route)
