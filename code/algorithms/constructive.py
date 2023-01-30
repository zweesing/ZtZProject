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
        super().__init__(start, end, board, size)

    def find(self):
        """
                Runs the constructive algoritme.

                Returns:
                    list with tuples of path taken, total wire count and the board, in that order.
        """
        start = [(self.start_gate_x, self.start_gate_y, 0)]
        explored = []
        queue = [start]
        counter = 0
        score_best_solution = 1000000
        solutions_counter = 0
        intersections = 0

        # implementations of depth and or breth search for determining route. Implement 3D part.
        while queue:
            # Next cell in the route is taken and a temporary node is made

            route = queue.pop(0)

            node = [route[-1]]

            counter += 1



            # Check if node has been explored already
            if node not in explored:
                #print(node)
                neighbours = self.find_neighbours(node)
                #print(neighbours)

                # The neighbours are checked and added to the route
                for neighbour in neighbours:
                    # print(node)
                    # print(neighbour)
                    neighbour_x = neighbour[0]
                    neighbour_y = neighbour[1]
                    neighbour_z = neighbour[2]
                    node_x, node_y, node_z = node[0]
                    #print('eerst ben ik hier')


                    if self.board[neighbour_z][neighbour_y][neighbour_x] != "0" and self.board[neighbour_z][neighbour_y][neighbour_x] != "X":
                        if node_x - 1 == neighbour_x and node_y == neighbour_y and node_z == neighbour_z and counter > 1:
                            if self.is_valid((neighbour_x - 1), neighbour_y, neighbour_z):
                                after_intersection = ((neighbour_x - 1), neighbour_y, neighbour_z)
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        if node_x + 1 == neighbour_x and node_y == neighbour_y and node_z == neighbour_z and counter > 1:
                            if self.is_valid((neighbour_x + 1), neighbour_y, neighbour_z):
                                after_intersection = ((neighbour_x + 1), neighbour_y, neighbour_z)
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1


                        if node_x == neighbour_x and node_y - 1 == neighbour_y and node_z == neighbour_z and counter > 1:
                            if self.is_valid(neighbour_x, (neighbour_y - 1), neighbour_z):
                                after_intersection = (neighbour_x, (neighbour_y - 1), neighbour_z)
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        if node_x == neighbour_x and node_y + 1 == neighbour_y and node_z == neighbour_z and counter > 1:
                            if self.is_valid(neighbour_x, (neighbour_y + 1), neighbour_z):
                                after_intersection = (neighbour_x, (neighbour_y + 1), neighbour_z)
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1


                        if node_x == neighbour_x and node_y == neighbour_y and node_z - 1 == neighbour_z and counter > 1:
                            if self.is_valid(neighbour_x, neighbour_y, (neighbour_z - 1)):
                                after_intersection = (neighbour_x, neighbour_y, (neighbour_z - 1))
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        if node_x == neighbour_x and node_y == neighbour_y and node_z + 1 == neighbour_z and counter > 1:
                            if self.is_valid(neighbour_x, neighbour_y, (neighbour_z - 1)):
                                after_intersection = (neighbour_x, neighbour_y, (neighbour_z + 1))
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        else:
                            explored.append(node)

                    else:
                        new_route = list(route)
                        new_route.append(neighbour)
                        queue.append(new_route)


                    # Check if the end point has been reached
                    if self.end_point(neighbour_x, neighbour_y, neighbour_z):
                        wire_count = len(new_route) - 1
                        intersection_count = intersections
                        score_new_route = wire_count + (300 * intersection_count)
                        solutions_counter += 1

                        if score_new_route < score_best_solution:
                            best_solution_route = new_route

                            score_best_solution = score_new_route

                intersections = 0
                explored.append(node)

            if solutions_counter == 5:
                break
            # If no node can be explored the connection can't be made and crashed is returned


        # Write down the route with "1" expect the gates, that must stay X.
        if solutions_counter >= 1:
            for coord in best_solution_route:
                coord_x = coord[0]
                coord_y = coord[1]
                coord_z = coord[2]
                if coord_x == self.end_gate_x and coord_y == self.end_gate_y and coord_z == 0:
                    continue
                elif coord_x == self.start_gate_x and coord_y == self.start_gate_y and coord_z == 0:
                    continue
                else:
                    self.board[coord_z][coord_y][coord_x] = "1"

            return best_solution_route, wire_count, self.board

        else:
            return 'crashed'






    def find_neighbours(self, node):
        """
                checks for the neighbours of a node and if they are inside the board.

                Args:
                    node (tuple): tuple with coordinates x, y and z

                Returns:
                    list of tuples, where the tuples are the coordinates of the neighbours of the node

        """
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
                if (self.size <= j or j <= 0) or (self.size <= i or i <= 0) or (self.size < k or k < -self.size):
                    neighbours[counter] = None
                    # print(neighbours)
                    counter += 1
                else:
                    counter += 1
                    continue

        return[i for i in neighbours if i is not None]

    def score_calculator(self, wire_count, intersections):
        print('hi:', intersections)
        cost = wire_count + 300 * intersections
        return cost
