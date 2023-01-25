from classes.pathfinder import Pathfinder
from classes.looptester import looptest
import random


class Pathfind(Pathfinder):
    """
    subclass of pathfinder class. This algorithm uses a sort of greedy algorithm to find the shortest route. 
    """

    def __init__(self, start, end, board, level):
        """
        runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            level (int): z coordinate
        """
        super().__init__(start, end, board)
        self.level = level

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
        current_gate_z = self.level
        current_gate_z = 0

        end_gate = [(self.end_gate_x, self.end_gate_y, 0)]

        random_direction = ["x", "y", "z"]
        random_direction2 = [1, -1]

        # start with x coordinate 
        while current_gate_x < self.end_gate_x:
            current_gate_x += 1

            # if the new current position has a z coordinate, it should be updated in the route list
            if current_gate_z != 0:
                current_position = (current_gate_x, current_gate_y, current_gate_z)
            else:
                current_position = (current_gate_x, current_gate_y)

            # if the wire has found the end gate, the loop breaks
            if self.end_point(current_gate_x, current_gate_y):
                route.append(current_position)
                wire_count += 1
                break

            # if the wire goes the wrong way it should choose the next direction randomly
            if not self.is_valid(current_position):
                current_gate_x -= 1

                current_gate_x_or_y = random.choice(random_direction)
                left_or_right = random.choice(random_direction2)

                if current_gate_x_or_y == "x":
                    current_gate_x += left_or_right
                elif current_gate_x_or_y == "y":
                    current_gate_y += left_or_right
                else:
                    current_gate_z += left_or_right

                if current_gate_z != 0:
                    current_position = (current_gate_x, current_gate_y, current_gate_z)
                else:
                    current_position = (current_gate_x, current_gate_y)

            # append the new current position and update the wire count
            route.append(current_position)
            wire_count += 1

            # vraag hoe dit moet met een 3d array
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

if __name__ == "__main__":
    gatesfilepath = "data/chip_0/print_0.csv"
    netlistpath = "data/chip_0/netlist_1.csv"
    total_counter = 0

    for solution in range(50):
        results = looptest(Pathfind, gatesfilepath, netlistpath, solution)

        path, routes, totalwirecount, crash_counter = results
        total_counter += crash_counter

    print(path)
    print(routes)
    print(totalwirecount)
    print(total_counter)