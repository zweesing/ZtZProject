from ..classes.pathfinder import Pathfinder


class Pathfind(Pathfinder):
    def __init__(self):
        super().__init__()

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
