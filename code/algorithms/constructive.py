from ..classes.pathfinder import Pathfinder
from code.classes.looptester import looptest


class Constructive(Pathfinder):
    """ Subclass for the pathfinder class. This Algoritme determines the shortest path using depth and breth search."""

    def __init__(self, start, end, board, size):
        """
        runs the init of pathfinder, which creates the nessecary class atributes.

        Args:
            start (tuple): tuple with start gate x and y
            end (tuple): tuple with end gate x and y
            board (list): nested list which contains the board with the gates
            level (int): z coordinate
        """
        self.size = size
        super().__init__(start, end, board)

    def find(self):
        start = [(self.start_gate_x, self.start_gate_y, 0)]
        explored = []
        queue = [start]

        # implementations of depth and or breth search for determining route. Implement 3D part.
        while queue:
            # Next cell in the route is taken and a temporary node is made
            route = queue.pop(0)
            #print(route)

            node = [route[-1]]


            # Check if node has been explored already
            if node not in explored:
                neighbours = self.find_neighbours(node)
                # print(neighbours)

                # The neighbours are checked and added to the route
                for neighbour in neighbours:
                    #print(neighbour)
                    neighbour_x = neighbour[0]
                    neighbour_y = neighbour[1]
                    neighbour_z = neighbour[2]

                    if self.board[neighbour_z][neighbour_y][neighbour_x] != "0" and self.board[neighbour_z][neighbour_y][neighbour_x] != "X":
                        explored.append(node)

                    else:

                        new_route = list(route)
                        new_route.append(neighbour)
                        queue.append(new_route)
                        wire_count = len(new_route) - 1

                        # Check if the end point has been reached
                        if neighbour_x == self.end_gate_x and neighbour_y == self.end_gate_y and neighbour_z == 0:

                            # Write down the route with "1" expect the gates, that must stay X.
                            for coord in new_route:
                                coord_x = coord[0]
                                coord_y = coord[1]
                                coord_z = coord[2]
                                if coord_x == self.end_gate_x and coord_y == self.end_gate_y and coord_z == 0:
                                    continue
                                elif coord_x == self.start_gate_x and coord_y == self.start_gate_y and coord_z == 0:
                                    continue
                                else:
                                    self.board[coord_z][coord_y][coord_x] = "1"

                            #print(new_route)
                            return new_route, wire_count, self.board

                explored.append(node)

        # If no node can be explored the connection can't be made and crashed is returned
        return "crashed"

    def find_neighbours(self, node):
        x, y, z = node[0]
        # print(x, y)

        neighbours = [
            (x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)
        ]
        counter = 0
        while counter < len(neighbours):

            for i, j, k, in neighbours:
                # print(i)
                # print(j)
                # print(counter)
                # get size from grid board instead of static 7.
                if (self.size <= j or j < 0) or (self.size <= i or i < 0) or (self.size <= k or k < 0):
                    neighbours[counter] = None
                    # print(neighbours)
                    counter += 1
                else:
                    counter += 1
                    continue

        return[i for i in neighbours if i is not None]
