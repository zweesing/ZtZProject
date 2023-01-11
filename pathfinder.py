class Pathfinder:
    def __init__(self, start, end, board):
        # Switched y and x to make sure the coordinates are read right.
        self.start_gate_x, self.start_gate_y = start
        self.end_gate_x, self.end_gate_y = end
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
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break
            if not self.is_valid(current_position):
                if current_gate_y < self.end_gate_y:
                    current_gate_x -= 1
                    current_gate_y += 1
                    current_position = (current_gate_x, current_gate_y)
                elif current_gate_y > self.end_gate_y:
                    current_gate_x -= 1
                    current_gate_y -= 1
                    current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_y][current_gate_x] = "1"

        while current_gate_x > self.end_gate_x:
            current_gate_x -= 1
            current_position = (current_gate_x, current_gate_y)
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break
            if not self.is_valid(current_position):
                if current_gate_y < self.end_gate_y:
                    current_gate_x += 1
                    current_gate_y += 1
                    current_position = (current_gate_x, current_gate_y)
                elif current_gate_y > self.end_gate_y:
                    current_gate_x += 1
                    current_gate_y -= 1
                    current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_y][current_gate_x] = "1"

        while current_gate_y < self.end_gate_y:
            current_gate_y += 1
            current_position = (current_gate_x, current_gate_y)
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break
            if not self.is_valid(current_position):
                if current_gate_x < self.end_gate_x:
                    current_gate_y -= 1
                    current_gate_x += 1
                    current_position = (current_gate_x, current_gate_y)
                elif current_gate_x > self.end_gate_x:
                    current_gate_y -= 1
                    current_gate_x -= 1
                    current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_y][current_gate_x] = "1"

        while current_gate_y > self.end_gate_y:
            current_gate_y -= 1
            current_position = (current_gate_x, current_gate_y)
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break
            if not self.is_valid(current_position):
                if current_gate_x < self.end_gate_x:
                    current_gate_y += 1
                    current_gate_x += 1
                    current_position = (current_gate_x, current_gate_y)
                elif current_gate_x > self.end_gate_x:
                    current_gate_y += 1
                    current_gate_x -= 1
                    current_position = (current_gate_x, current_gate_y)
            route.append(current_position)
            wire_count += 1
            self.board[current_gate_y][current_gate_x] = "1"

        return route, wire_count, self.board

    def is_valid(self, next_position):
        if next_position == '0':
            return True

    def end_point(self, next_position_x, next_position_y):
        if next_position_x == self.end_gate_x and next_position_y == self.end_gate_y:
            return True



    def __repr__(self):
        return "\n".join([" ".join(row) for row in self.board])
