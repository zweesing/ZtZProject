from ..classes.pathfinder import Pathfinder
import random


class Pathfindrandom(Pathfinder):
    """
    Subclass of pathfinder class. this uses a completely random algorithm to find a route.
    """

    def __init__(self, start, end, board, size):
        """
        Runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            size (int): size of the board
        """

        super().__init__(start, end, board, size)

    def find(self):
        """
        The algorithm itself. Finds a random route for each connection.

        Returns:
            list with tuples of path taken, total wire count and the board, in that order.
        """

        route = [(self.start_gate_x, self.start_gate_y, 0)]
        wire_count = 0
        current_gate_x = self.start_gate_x
        current_gate_y = self.start_gate_y

        crash_counter = 0

        # Make a list with x and y
        random_direction = ["x", "y"]

        # Make a list with 1 and -1
        random_direction2 = [1, -1]

        while True:
            # Choose randomly between x, y
            current_gate_x_or_y = random.choice(random_direction)

            # Choose randomly between -1 or 1
            left_or_right = random.choice(random_direction2)

            # Move to the chosen random direction
            if current_gate_x_or_y == "x":
                current_gate_x += left_or_right
            else:
                current_gate_y += left_or_right

            # Change the current position 
            current_position = (current_gate_x, current_gate_y, 0)

            # Check if end gate has been reached
            if self.end_point(current_gate_x, current_gate_y, 0):
                route.append(current_position)
                wire_count += 1
                break

            # Check if new position is valid
            if not self.is_valid(current_gate_x, current_gate_y, 0):

                # If not valid move a back
                if current_gate_x_or_y == "x":
                    current_gate_x += -1 * left_or_right
                else:
                    current_gate_y += -1 * left_or_right
                
                # Change the position back
                current_position = (current_gate_x, current_gate_y, 0)

                # Add crash
                crash_counter += 1

            # If it was valid, append the current position to the route and set crash counter back to 0
            else:
                route.append(current_position)
                wire_count += 1
                self.board[0][current_gate_y][current_gate_x] = "1"

                crash_counter == 0

            # If the crash counter is more than 20 the algorithm should crash
            if crash_counter > 20:
                return "crashed"

        return route, wire_count, self.board