from ..classes.pathfinder import Pathfinder
from code.classes.looptester import looptest


class Constructive(Pathfinder):
    """ Subclass for the pathfinder class. This Algoritme determines the shortest path using depth and breth search."""

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
        start = [(self.start_gate_x, self.start_gate_y)]
        explored = []
        queue = [[start]]
        # implementations of depth and or breth search for determining route. Implement 3D part.
        while queue:
            route = queue.pop(0)
            node = route[-1]
            print(node)
            print(22)

            if node not in explored:
                neighbours = self.find_neighbours(node)
                print(neighbours)

                for neighbour in neighbours:
                    new_route = list(route)
                    new_route.append(neighbour)
                    queue.append(new_route)

                    # if neighbour is self.end_point(neighbour_x, neighbour_y):
                    #     return new_route

                explored.append(node)
        return route


