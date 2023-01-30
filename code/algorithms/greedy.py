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

        self.wire_count = 0
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

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_pos_and_route()
                    return self.route, self.wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_x -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)

                    # try a random step
                    if not self.go_random_direction():
                        # if no random step can be found, try a greedy intersection
                        # if not self.greedy_intersection():
                        # then try a greedy intersection. otherwise crash
                        if not self.go_random_intersection():
                            return "crashed"

                # append the new current position and update the wire count
                self.update_pos_and_route()

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # second x direction
            while self.current_x > self.end_gate_x:
                self.current_x -= 1

                # if the new current position has a z coordinate, it should be updated in the self.route list

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_pos_and_route()
                    return self.route, self.wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_x += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)

                    # try a random step
                    if not self.go_random_direction():
                        # if no random step can be found, try a greedy intersection
                        # if not self.greedy_intersection():
                        # then try a greedy intersection. otherwise crash
                        if not self.go_random_intersection():
                            return "crashed"

                # append the new current position and update the wire count
                self.update_pos_and_route()

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # y direction
            while self.current_y < self.end_gate_y:
                self.current_y += 1

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_pos_and_route()
                    return self.route, self.wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_y -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        # if no random step can be found, try a greedy intersection
                        # if not self.greedy_intersection():
                        # then try a greedy intersection. otherwise crash
                        if not self.go_random_intersection():
                            return "crashed"

                # append the new current position and update the wire count
                self.update_pos_and_route()

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # second y direction
            while self.current_y > self.end_gate_y:
                self.current_y -= 1

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_pos_and_route()
                    return self.route, self.wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_y += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        # if no random step can be found, try a greedy intersection
                        # if not self.greedy_intersection():
                        # then try a greedy intersection. otherwise crash
                        if not self.go_random_intersection():
                            return "crashed"

                # append the new current position and update the wire count
                self.update_pos_and_route()

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # z positive
            while self.current_z < 0:
                self.current_z += 1

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_pos_and_route()
                    self.wire_count += 1
                    return self.route, self.wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_z -= 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        # if no random step can be found, try a greedy intersection
                        # if not self.greedy_intersection():
                        # then try a greedy intersection. otherwise crash
                        if not self.go_random_intersection():
                            return "crashed"

                # append the new current position and update the wire count
                self.update_pos_and_route()

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

            # z negative
            while self.current_z > 0:
                self.current_z -= 1

                # if the wire has found the end gate, the loop breaks
                if self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_pos_and_route()
                    return self.route, self.wire_count, self.board

                # if the wire goes the wrong way it should choose the other directions randomly
                if not self.is_valid(self.current_x, self.current_y, self.current_z):
                    self.current_z += 1

                    # shuffle lists and check if a random astep can be made
                    random.shuffle(self.random_direction)
                    random.shuffle(self.random_direction2)
                    # try a random step
                    if not self.go_random_direction():
                        # if no random step can be found, try a greedy intersection
                        # if not self.greedy_intersection():
                        # then try a greedy intersection. otherwise crash
                        if not self.go_random_intersection():
                            return "crashed"

                # append the new current position and update the wire count
                self.update_pos_and_route()

                # vraag hoe dit moet met een 3d array
                self.board[self.current_z][self.current_y][self.current_x] = "1"

    def go_random_direction(self):
        """loop through all possible directions and see if you can go in any of those.
        update coordinates and return True if a valid random step has been found"""
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
        """Search through all directions to see if a random intersection step can be made.
        updates the route to include the intersection and update coordinatesif a valid path is found, and return True"""
        for xyz in self.random_direction:
            for left_right in self.random_direction2:
                if xyz == "x" and self.is_valid(
                    self.current_x + 2 * left_right,
                    self.current_y,
                    self.current_z,
                ):
                    # make two steps, so add the intersection point manually

                    self.current_x += left_right
                    self.update_pos_and_route()
                    self.current_x += left_right
                    return True

                elif xyz == "y" and self.is_valid(
                    self.current_x,
                    self.current_y + 2 * left_right,
                    self.current_z,
                ):
                    self.current_y += left_right
                    self.update_pos_and_route()
                    self.current_y += left_right
                    return True

                elif xyz == "z" and self.is_valid(
                    self.current_x,
                    self.current_y,
                    self.current_z + 2 * left_right,
                ):
                    self.current_z += left_right
                    self.update_pos_and_route()
                    self.current_z += left_right
                    return True

    def greedy_intersection(self):
        """Check all directions to see if a greedy intersection can be made, and then make it and return True."""
        # positive x
        if self.current_x < self.end_gate_x and self.is_valid(
            self.current_x + 2,
            self.current_y,
            self.current_z,
        ):
            self.current_x + 1
            self.update_pos_and_route()
            self.current_x + 1
            return True

        # negative x
        if self.current_x > self.end_gate_x and self.is_valid(
            self.current_x - 2,
            self.current_y,
            self.current_z,
        ):
            self.current_x - 1
            self.update_pos_and_route()
            self.current_x - 1
            return True

        # positive y
        if self.current_y < self.end_gate_y and self.is_valid(
            self.current_x,
            self.current_y + 2,
            self.current_z,
        ):
            self.current_y + 1
            self.update_pos_and_route()
            self.current_y + 1
            return True

        # negative y
        if self.current_y > self.end_gate_y and self.is_valid(
            self.current_x,
            self.current_y - 2,
            self.current_z,
        ):
            self.current_y - 1
            self.update_pos_and_route()
            self.current_y - 1
            return True

        # positive z
        if self.current_z < 0 and self.is_valid(
            self.current_x,
            self.current_y,
            self.current_z + 2,
        ):
            self.current_z + 1
            self.update_pos_and_route()
            self.current_z + 1
            return True

        # negative z
        if self.current_z > 0 and self.is_valid(
            self.current_x,
            self.current_y,
            self.current_z - 2,
        ):
            self.current_z - 1
            self.update_pos_and_route()
            self.current_z - 1
            return True

    def update_pos_and_route(self):
        """append the current position to the route"""
        current_position = (
            self.current_x,
            self.current_y,
            self.current_z,
        )
        self.route.append(current_position)
        self.wire_count += 1
