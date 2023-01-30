from ..classes.pathfinder import Pathfinder
import random


class Pathfind(Pathfinder):
    """
    subclass of pathfinder class. This algorithm uses a sort of greedy algorithm to find the shortest self.route.
    """

    def __init__(self, start, end, board, size):
        """
        runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            level (int): z coordinate
        """
        super().__init__(start, end, board, size)

    def find(self):
        """
        the algorithm finds the shortest path between two gates by checking the relative position.
        If the path is blocked in one direction, it picks a new direction randomly.
        This new direction could also be up or down to a new layer.

        Returns:
            list with tuples of path taken, total wire count and the board, in that order.
        """
        self.route = [(self.start_gate_x, self.start_gate_y, 0)]

        wire_count = 0
        self.current_x = self.start_gate_x
        self.current_y = self.start_gate_y
        self.current_z = 0

        self.random_direction = ["x", "y", "z"]
        self.random_direction2 = [1, -1]

        while True:
            # start with x coordinate
            while self.current_x < self.end_gate_x:
                self.current_x += 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                current_position = (self.current_x, self.current_y, self.current_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.route.append(current_position)
                    wire_count += 1
                    return self.route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_x -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)

                    # try a random step
                    if not self.go_random_direction():
                        if not self.go_random_intersection():
                            return "crashed"

                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )

                # append the new current position and update the wire count
                self.route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # second x direction
            while self.current_x > self.end_gate_x:
                self.current_x -= 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                current_position = (self.current_x, self.current_y, self.current_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.route.append(current_position)
                    wire_count += 1
                    return self.route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_x += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)

                    # try a random step
                    if not self.go_random_direction():
                        if not self.go_random_intersection():
                            return "crashed"

                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )

                # append the new current position and update the wire count
                self.route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # y direction
            while self.current_y < self.end_gate_y:
                self.current_y += 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                current_position = (self.current_x, self.current_y, self.current_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.route.append(current_position)
                    wire_count += 1
                    return self.route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_y -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        if not self.go_random_intersection():
                            return "crashed"

                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )

                # append the new current position and update the wire count
                self.route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # second y direction
            while self.current_y > self.end_gate_y:
                self.current_y -= 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                current_position = (self.current_x, self.current_y, self.current_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.route.append(current_position)
                    wire_count += 1
                    return self.route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_y += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        if not self.go_random_intersection():
                            return "crashed"

                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )

                # append the new current position and update the wire count
                self.route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # z positive
            while self.current_z < 0:
                self.current_z += 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                current_position = (self.current_x, self.current_y, self.current_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.route.append(current_position)
                    wire_count += 1
                    return self.route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_z -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        if not self.go_random_intersection():
                            return "crashed"

                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )

                # append the new current position and update the wire count
                self.route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # z negative
            while self.current_z > 0:
                self.current_z -= 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                current_position = (self.current_x, self.current_y, self.current_z)

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.route.append(current_position)
                    wire_count += 1
                    return self.route, wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_z += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        if not self.go_random_intersection():
                            return "crashed"

                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )

                # append the new current position and update the wire count
                self.route.append(current_position)
                wire_count += 1

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

    def go_random_direction(self):
        for xyz in self.random_direction:
            for left_right in self.random_direction2:
                if xyz == "x" and self.is_valid(
                    self.current_x + left_right,
                    self.current_y,
                    self.current_z,
                ):
                    self.current_x += left_right
                    return True

                if xyz == "y" and self.is_valid(
                    self.current_x,
                    self.current_y + left_right,
                    self.current_z,
                ):
                    self.current_y += left_right
                    return True

                if xyz == "z" and self.is_valid(
                    self.current_x,
                    self.current_y,
                    self.current_z + left_right,
                ):
                    self.current_z += left_right
                    return True

    def go_random_intersection(self):
        for xyz in self.random_direction:
            for left_right in self.random_direction2:
                if xyz == "x" and self.is_valid(
                    self.current_x + 2 * left_right,
                    self.current_y,
                    self.current_z,
                ):
                    # make two steps, so add the intersection point manually

                    self.current_x += left_right
                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )
                    self.route.append(current_position)
                    self.current_x += left_right
                    return True

                elif xyz == "y" and self.is_valid(
                    self.current_x,
                    self.current_y + 2 * left_right,
                    self.current_z,
                ):
                    self.current_y += left_right
                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )
                    self.route.append(current_position)
                    self.current_y += left_right
                    return True

                elif xyz == "z" and self.is_valid(
                    self.current_x,
                    self.current_y,
                    self.current_z + 2 * left_right,
                ):
                    self.current_z += left_right
                    current_position = (
                        self.current_x,
                        self.current_y,
                        self.current_z,
                    )
                    self.route.append(current_position)
                    self.current_z += left_right
                    return True
