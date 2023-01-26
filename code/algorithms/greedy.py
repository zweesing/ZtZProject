from ..classes.pathfinder import Pathfinder
import random


class Pathfind(Pathfinder):
    """
    subclass of pathfinder class. This algorithm uses a sort of greedy algorithm to find the shortest route.
    """

    def __init__(self, start, end, board):
        """
        runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            level (int): z coordinate
        """
        super().__init__(start, end, board)

    def find(self):
        """
        the algorithm finds the shortest path between two gates by checking the relative position.
        If the path is blocked in one direction, it picks a new direction randomly.
        This new direction could also be up or down to a new layer.

        Returns:
            list with tuples of path taken, total wire count and the board, in that order.
        """
        route = [(self.start_gate_x, self.start_gate_y)]

        wire_count = 0
        current_gate_x = self.start_gate_x
        current_gate_y = self.start_gate_y
        current_gate_z = 0

        end_gate = [(self.end_gate_x, self.end_gate_y)]

        random_direction = ["x", "y"]
        random_direction2 = [1, -1]

        # start with x coordinate
        while current_gate_x < self.end_gate_x:
            current_gate_x += 1

            # if the new current position has a z coordinate, it should be updated in the route list

            current_position = (current_gate_x, current_gate_y)

            print(current_gate_x)
            print(current_gate_y)
            print(current_gate_z)
            # if the wire has found the end gate, the loop breaks
            if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                route.append(current_position)
                wire_count += 1
                break

            # if the wire goes the wrong way it should choose the next direction randomly
            if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                current_gate_x -= 1

                current_gate_x_or_y = random.choice(random_direction)
                left_or_right = random.choice(random_direction2)

                if current_gate_x_or_y == "x":
                    current_gate_x += left_or_right
                else:
                    current_gate_y += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    if current_gate_x_or_y == "x":
                        # maak de tweede ook random ipv altijd van foute x richting gelijk naar de andere richting overstappen
                        current_gate_x += -1 * left_or_right
                        current_gate_y += left_or_right
                    else:
                        current_gate_y += -1 * left_or_right
                        current_gate_x += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    print("crashed")
                    return "crashed"
                else:
                    current_position = (current_gate_x, current_gate_y)

            # append the new current position and update the wire count
            route.append(current_position)
            wire_count += 1

            # vraag hoe dit moet met een 3d array
            self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

        # second x direction
        while current_gate_x > self.end_gate_x:
            current_gate_x -= 1

            # if the new current position has a z coordinate, it should be updated in the route list

            current_position = (current_gate_x, current_gate_y)
            print(current_gate_x)
            print(current_gate_y)
            print(current_gate_z)

            # if the wire has found the end gate, the loop breaks
            if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                route.append(current_position)
                wire_count += 1
                break

            # if the wire goes the wrong way it should choose the next direction randomly
            if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                current_gate_x += 1

                current_gate_x_or_y = random.choice(random_direction)
                left_or_right = random.choice(random_direction2)

                if current_gate_x_or_y == "x":
                    current_gate_x += left_or_right
                else:
                    current_gate_y += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    if current_gate_x_or_y == "x":
                        current_gate_x += -1 * left_or_right
                        current_gate_y += left_or_right
                    else:
                        current_gate_y += -1 * left_or_right
                        current_gate_x += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    print("crashed")
                    return "crashed"
                else:
                    current_position = (current_gate_x, current_gate_y)

            # append the new current position and update the wire count
            route.append(current_position)
            wire_count += 1

            # vraag hoe dit moet met een 3d array
            self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

        # y direction
        while current_gate_y < self.end_gate_y:
            current_gate_y += 1

            # if the new current position has a z coordinate, it should be updated in the route list

            current_position = (current_gate_x, current_gate_y)
            print(current_gate_x)
            print(current_gate_y)
            print(current_gate_z)

            # if the wire has found the end gate, the loop breaks
            if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                route.append(current_position)
                wire_count += 1
                break

            # if the wire goes the wrong way it should choose the next direction randomly
            if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                current_gate_y -= 1

                current_gate_x_or_y = random.choice(random_direction)
                left_or_right = random.choice(random_direction2)

                if current_gate_x_or_y == "x":
                    current_gate_x += left_or_right
                else:
                    current_gate_y += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    if current_gate_x_or_y == "x":
                        current_gate_x += -1 * left_or_right
                        current_gate_y += left_or_right
                    else:
                        current_gate_y += -1 * left_or_right
                        current_gate_x += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    print("crashed")
                    return "crashed"
                else:
                    current_position = (current_gate_x, current_gate_y)

            # append the new current position and update the wire count
            route.append(current_position)
            wire_count += 1

            # vraag hoe dit moet met een 3d array
            self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

        # second y direction
        while current_gate_y > self.end_gate_y:
            current_gate_y -= 1

            # if the new current position has a z coordinate, it should be updated in the route list

            current_position = (current_gate_x, current_gate_y)
            print(current_gate_x)
            print(current_gate_y)
            print(current_gate_z)

            # if the wire has found the end gate, the loop breaks
            if self.end_point(current_gate_x, current_gate_y, current_gate_z):
                route.append(current_position)
                wire_count += 1
                break

            # if the wire goes the wrong way it should choose the next direction randomly
            if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                current_gate_y += 1

                current_gate_x_or_y = random.choice(random_direction)
                left_or_right = random.choice(random_direction2)

                if current_gate_x_or_y == "x":
                    current_gate_x += left_or_right
                else:
                    current_gate_y += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    if current_gate_x_or_y == "x":
                        current_gate_x += -1 * left_or_right
                        current_gate_y += left_or_right
                    else:
                        current_gate_y += -1 * left_or_right
                        current_gate_x += left_or_right

                if not self.is_valid(current_gate_x, current_gate_y, current_gate_z):
                    print("crashed")
                    return "crashed"
                else:
                    current_position = (current_gate_x, current_gate_y)

            # append the new current position and update the wire count
            route.append(current_position)
            wire_count += 1

            # vraag hoe dit moet met een 3d array
            self.board[current_gate_z][current_gate_y][current_gate_x] = "1"

        print(route)

        return route, wire_count, self.board
