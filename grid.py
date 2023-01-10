class Grid():
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.board = []

    def get_board(self):
        # Function makes a board based on the column and row input of the user
        for row in range(self.row):
            self.board.append([])
            for width in range(self.column):
                self.board[row].append('0')
        return self.board

    def place_gate(self, column, row):
        # Places a gate at the coordinates given by the user
        self.board[column][row] = 'X'

    def __repr__(self):
        return '\n'.join([' '.join(row) for row in self.board])


if __name__ == '__main__':
    g = Grid(10, 10)
    g.get_board()
    print(g)
    print()
    g.place_gate(4, 4)
    print(g)
