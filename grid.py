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


class Pathfinder:
    def __init__(self, start_gate_x, start_gate_y, end_gate_x, end_gate_y, board):
        self.start_gate_x = start_gate_x
        self.start_gate_y = start_gate_y
        self.end_gate_x = end_gate_x
        self.end_gate_y = end_gate_y
        self.board = board

    def find(self):
        route = [(self.start_gate_x, self.start_gate_y)]
        wire_count = 0
        current_gate_x = self.start_gate_x
        current_gate_y = self.start_gate_y
        end_gate = [(self.end_gate_x, self.end_gate_y)]

        # For now only checking first one direction then other. Not switching when stuck
        # Fix End gate needs if statement to return to a X
        while current_gate_x < self.end_gate_x:
            current_gate_x += 1
            current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_x][current_gate_y] = "1"
            if current_position == end_gate:
                self.board[current_gate_x][current_gate_y] = "X"

        while current_gate_x > self.end_gate_x:
            current_gate_x += 1
            current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_x][current_gate_y] = "1"
            if current_position == end_gate:
                self.board[current_gate_x][current_gate_y] = "X"

        while current_gate_y < self.end_gate_y:
            current_gate_y += 1
            current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_x][current_gate_y] = "1"
            if current_position == end_gate:
                self.board[current_gate_x][current_gate_y] = "X"

        while current_gate_y > self.end_gate_y:
            current_gate_y += 1
            current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_x][current_gate_y] = "1"
            if current_position == end_gate:
                self.board[current_gate_x][current_gate_y] = "X"

        return route, wire_count, self.board

    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])


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
    g = Pathfinder(0, 0, 4, 4, b)
    print(p)
    print()
    route, wire_count, board = g.find()
    print(g)
    print(route)
