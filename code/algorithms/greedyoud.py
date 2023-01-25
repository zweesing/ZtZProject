from ..classes.pathfinder import Pathfinder


class Pathfind(Pathfinder):
    """subclass of pathfinder class. This contains our first pathfinder algorithm,
    and uses a sort of greedy algorithm to find the shortest route. doesnt always work for multiple paths.
    """

    def __init__(self, start, end, board):
        """runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
        """
        super().__init__(start, end, board)


    def find(self):
        """the algoritm. finds the shortest path between two gates by checking the relative position.
        If the path is blocked in one direction, it tries to go around. Does not work yet if the path is blocked in one direction and the other direction is already correct.

        Returns:
            list with tuples of path taken, total wire count and the board, in that order.
        """
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

