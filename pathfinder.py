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
