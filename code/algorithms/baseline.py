from ..classes.pathfinder import Pathfinder
import random

# Random algoritme maken die een random kant kiest om op te gaan


class Pathfindrandom(Pathfinder):
    """subclass of pathfinder class. this uses a completely random algorithm to find a route."""

    def __init__(self, start, end, board):
        """Runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
        """
        super().__init__(start, end, board)

    def find(self):
        """The algorithm itself.

        Returns:
            list with tuples of path taken, total wire count and the board, in that order.
        """
        route = [(self.start_gate_x, self.start_gate_y)]
        wire_count = 0
        current_gate_x = self.start_gate_x
        current_gate_y = self.start_gate_y

        crash_counter = 0

        while True:
            # hier moet hij dus een random kant kiezen om op te gaan

            # maak een lijst aan met x en y
            random_direction = ["x", "y"]

            # maak een lijst aan met 1 en -1 (of hij naar links, rechts of boven of beneden moet)
            random_direction2 = [1, -1]

            # kies random uit x of y
            current_gate_x_or_y = random.choice(random_direction)

            # kies random -1 of 1
            left_or_right = random.choice(random_direction2)

            # hier heeft hij dus random uitgekozen of hij naar x of y gaat en of hij plus 1 of min 1 doet.
            # Hier wordt dat geimplementeerd.
            if current_gate_x_or_y == "x":
                current_gate_x += left_or_right
            else:
                current_gate_y += left_or_right

            # na de random kant gekozen te hebben veranderd de current position hier
            current_position = (current_gate_x, current_gate_y)

            # als hij bij de gate is moet hij wel nog stoppen
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break

            # Als de kant die hij kiest niet valid is moet hij wel nog een andere kant op.
            # Deze nieuwe kant moet dan ook random zijn.
            # Dit moet hij blijven doen tot hij een positie vindt die wel valid is. Daarom dus een while loop.
            if not self.is_valid(current_gate_x, current_gate_y):

                # Als hij niet de juiste kant op is gegaan moet hij dus terug op de juiste random as.
                # We weten welke as dit is omdat we het hebben opgeslagen in current_gate_x_or_y.
                # Door daarna left_or_right om te draaien kunnen we dus een stap terug.
                if current_gate_x_or_y == "x":
                    current_gate_x += -1 * left_or_right
                else:
                    current_gate_y += -1 * left_or_right

                current_position = (current_gate_x, current_gate_y)

                crash_counter += 1
            else:
                route.append(current_position)
                wire_count += 1
                self.board[current_gate_y][current_gate_x] = "1"

                crash_counter == 0

            if crash_counter > 20:
                return "crashed"

        return route, wire_count, self.board
