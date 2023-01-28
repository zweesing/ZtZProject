# algoritme zoekt snelste pad
# randomise lengte stap of breedte stap, maar ga wel volgens snelste pad, veel if statements
#  mag niet over andere gates heen.

# ideas:
# a left right connection a l, a up down connection is u, and a corner connection is c? then we can see if we can cross
# not checking if a step is valid, but for the fixer we need to check if the routes overlap regardless.
# maybe reading them in from the output?
from code.classes.pathfinder import Pathfinder
import random


class Pathfind_GR(Pathfinder):
    def __init__(self, start, end, board, size):
        super().__init__(start, end, board)

    def find(self):
        # a greedy algorithm that uses random steps if it gets stuck

        # list to save route in. a gate is always at z=0
        self.route = [(self.start_gate_x, self.start_gate_y, 0)]
        self.wire_count = 0

        self.current_x, self.current_y, self.current_z = (
            self.start_gate_x,
            self.start_gate_y,
            0,
        )

        # random element
        random_direction = ["x", "y", "z"]
        random_direction2 = [1, -1]

        crash_counter = 0

        # loop that finds path
        while True:

            # if it should go in that direction, and that is a valid step, make the step. if its the end gate, return
            # if no steps are made, choose a random direction and if that fails multiple times, start over
            made_step = False

            if crash_counter > 50:
                return "crashed"

            # X ------------------------------------------------------------
            # this sucks sorry but i kept making mistakes and this should work
            if self.current_x < self.end_gate_x and (
                self.is_valid(self.current_x + 1, self.current_y, self.current_z)
                or self.end_point(self.current_x + 1, self.current_y, self.current_z)
            ):
                self.current_x += 1

                self.update_route()
                made_step = True
                if not self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_board()
                else:
                    return self.route, self.wire_count, self.board

            elif self.current_x > self.end_gate_x and (
                self.is_valid(self.current_x - 1, self.current_y, self.current_z)
                or self.end_point(self.current_x - 1, self.current_y, self.current_z)
            ):
                self.current_x -= 1

                self.update_route()
                made_step = True

                if not self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_board()
                else:
                    return self.route, self.wire_count, self.board

            # Y ------------------------------------------------------------
            if self.current_y < self.end_gate_y and (
                self.is_valid(self.current_x, self.current_y + 1, self.current_z)
                or self.end_point(self.current_x, self.current_y + 1, self.current_z)
            ):
                self.current_y += 1

                self.update_route()
                made_step = True

                if not self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_board()
                else:
                    return self.route, self.wire_count, self.board

            elif self.current_y > self.end_gate_y and (
                self.is_valid(self.current_x, self.current_y - 1, self.current_z)
                or self.end_point(self.current_x, self.current_y - 1, self.current_z)
            ):
                self.current_y -= 1

                self.update_route()
                made_step = True

                if not self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_board()
                else:
                    return self.route, self.wire_count, self.board

            # Z ------------------------------------------------------------
            if self.current_z < 0 and (
                self.is_valid(self.current_x, self.current_y, self.current_z + 1)
                or self.end_point(self.current_x, self.current_y, self.current_z + 1)
            ):
                self.current_z += 1

                self.update_route()
                made_step = True

                if not self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_board()
                else:
                    return self.route, self.wire_count, self.board

            elif self.current_z > 0 and (
                self.is_valid(self.current_x, self.current_y, self.current_z - 1)
                or self.end_point(self.current_x, self.current_y, self.current_z - 1)
            ):
                self.current_z -= 1

                self.update_route()
                made_step = True

                if not self.end_point(self.current_x, self.current_y, self.current_z):
                    self.update_board()
                else:
                    return self.route, self.wire_count, self.board

            # random direction if it cant go where it needs to
            # other idea: make a list of all 6 options and just check those. shuffle them before every attempt
            if not made_step:
                current_gate_x_or_y = random.choice(random_direction)
                left_or_right = random.choice(random_direction2)

                if current_gate_x_or_y == "x" and self.is_valid(
                    self.current_x + left_or_right, self.current_y, self.current_z
                ):
                    self.current_x += left_or_right
                    self.update_route()
                    self.update_board()

                elif current_gate_x_or_y == "y" and self.is_valid(
                    self.current_x, self.current_y + left_or_right, self.current_z
                ):
                    self.current_y += left_or_right
                    self.update_route()
                    self.update_board()
                elif current_gate_x_or_y == "z" and self.is_valid(
                    self.current_x, self.current_y, self.current_z + left_or_right
                ):
                    self.current_y += left_or_right
                    self.update_route()
                    self.update_board()
                else:
                    crash_counter += 1
            else:
                crash_counter = 0

    def update_board(self):
        print(f"x: {self.current_x}, y: {self.current_y}")
        self.board[self.current_z][self.current_y][self.current_x] = "1"

    def update_route(self):
        self.route.append((self.current_x, self.current_y, self.current_z))
        self.wire_count += 1


# als conflict:
# check ander snelste pad?, anders laat het voor nu
# zo min mogelijk conflicten over, daarna bruggetjes maken proberen
