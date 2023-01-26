# algoritme zoekt snelste pad
# randomise lengte stap of breedte stap, maar ga wel volgens snelste pad, veel if statements
#  mag niet over andere gates heen.

# ideas:
# a left right connection a l, a up down connection is u, and a corner connection is c? then we can see if we can cross
# not checking if a step is valid, but for the fixer we need to check if the routes overlap regardless.
# maybe reading them in from the output?
from ..classes.pathfinder import Pathfinder
import random


class Pathfind(Pathfinder):
    def __init__(self, start, end, board):
        super().__init__(start, end, board)

    def find(self):
        # a greedy algorithm dat does not take conflict into account.

        # list to save route in. a gate is always at z=0
        self.route = [(self.start_gate_x, self.start_gate_y, 0)]
        self.wire_count = 0

        self.current_x, self.current_y, self.current_z = (
            self.start_gate_x,
            self.start_gate_y,
            0,
        )

        # loop that finds path
        while True:
            # this should take a step if it needs to, and if its not the end gate, it will update the board and keep going.

            # right
            if self.current_x < self.end_gate_x:
                self.current_x += 1
                self.update_route()
                if not self.end_point(self.current_x, self.current_y):
                    self.update_board()
                else:
                    return

            # left
            if self.current_x > self.end_gate_x:
                self.current_x -= 1
                self.update_route()
                if not self.end_point(self.current_x, self.current_y):
                    self.update_board()
                else:
                    return
            # up
            if self.current_y < self.end_gate_y:
                self.current_y += 1
                self.update_route()
                if not self.end_point(self.current_x, self.current_y):
                    self.update_board()
                else:
                    return
            # down
            if self.current_y > self.end_gate_y:
                self.current_y += 1
                self.update_route()
                if not self.end_point(self.current_x, self.current_y):
                    self.update_board()
                else:
                    return

    def update_board(self):
        self.board[self.current_z][self.current_y][self.current_x] = 1

    def update_route(self):
        self.route.append((self.current_x, self.current_y, 0))
        self.wire_count += 1


# als conflict:
# check ander snelste pad?, anders laat het voor nu
# zo min mogelijk conflicten over, daarna bruggetjes maken proberen
