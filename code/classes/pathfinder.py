class Pathfinder:
    def __init__(self, start, end, board, size):
        """Create class attributes needed for the different pathfind algorithms.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
        """
        # Switched y and x to make sure the coordinates are read right.
        self.start_gate_x, self.start_gate_y = start
        self.end_gate_x, self.end_gate_y = end
        self.board = board
        self.size = size

    def is_valid(self, next_position_x, next_position_y, next_position_z):
        """checks if a position is valid to move to,
        so not out of bounds, and not already visited, not another gate

        Args:
            next_position_x (int): x position on board
            next_position_y (int): y position on board

        Returns:
            bool: valid or not
        """

        if (
            (0 <= next_position_x < self.size)
            and (0 <= next_position_y < self.size)
            and (self.board[next_position_z][next_position_y][next_position_x] == "0")
            and (-self.size < next_position_z < self.size)
        ):

            return True

    def end_point(self, next_position_x, next_position_y, next_position_z):
        """checks if the goal gate is reached

        Args:
            next_position_x (int): x position on board
            next_position_y (int): y position on board
            next_position_z (int): z position on board

        Returns:
            bool: gate reached or not
        """
        if (
            next_position_x == self.end_gate_x
            and next_position_y == self.end_gate_y
            and next_position_z == 0
        ):
            return True

    def __repr__(self):
        """representation of the board"""
        return "\n".join([" ".join(row) for row in self.board[0]])
