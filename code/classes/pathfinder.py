class Pathfinder:
    def __init__(self, start, end, board):
        # Switched y and x to make sure the coordinates are read right.
        self.start_gate_x, self.start_gate_y = start
        self.end_gate_x, self.end_gate_y = end
        self.board = board

    def is_valid(self, next_position_x, next_position_y):
        if (0 <= next_position_x < len(self.board)) and (0 <= next_position_y < len(self.board)):
            if self.board[next_position_y][next_position_x] == "0":
                return True


    def end_point(self, next_position_x, next_position_y):
        if next_position_x == self.end_gate_x and next_position_y == self.end_gate_y:
            return True

    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])
