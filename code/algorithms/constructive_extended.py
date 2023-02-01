from ..classes.pathfinder import Pathfinder
from code.classes.looptester import looptest


class ConstructiveExtended(Pathfinder):
    """Subclass for the pathfinder class. This Algoritme determines the shortest path using depth and breth search."""

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

        # Keeps exploring nodes until the queue list is empty
        while queue:

            # Next node from the queue is taken and a temporary node is made
            route = queue.pop(0)
            node = [route[-1]]
            counter += 1

            # Check if node has been explored
            if node not in explored:
                # All the neighbours of the temporary node are found
                neighbours = self.find_neighbours(node)

                # Each neighbour is checked, if it is a valid step or if it is the end point
                for neighbour in neighbours:
                    neighbour_x = neighbour[0]
                    neighbour_y = neighbour[1]
                    neighbour_z = neighbour[2]
                    node_x, node_y, node_z = node[0]

                    # Check if the neighbour is a valid step
                    if (
                        self.board[neighbour_z][neighbour_y][neighbour_x] != "0"
                        and self.board[neighbour_z][neighbour_y][neighbour_x] != "X"
                    ):
                        # Check in which direction the wire is moving
                        if (
                            node_x - 1 == neighbour_x
                            and node_y == neighbour_y
                            and node_z == neighbour_z
                            and counter > 1
                        ):
                            # Check if an intersection can be made
                            if self.is_valid(
                                (neighbour_x - 1), neighbour_y, neighbour_z
                            ):
                                # Route is appended and intersection is counted
                                after_intersection = (
                                    (neighbour_x - 1),
                                    neighbour_y,
                                    neighbour_z,
                                )
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        # Check in which direction the wire is moving
                        if (
                            node_x + 1 == neighbour_x
                            and node_y == neighbour_y
                            and node_z == neighbour_z
                            and counter > 1
                        ):
                            # Check if an intersection can be made
                            if self.is_valid(
                                (neighbour_x + 1), neighbour_y, neighbour_z
                            ):
                                # Route is appended and intersection is counted
                                after_intersection = (
                                    (neighbour_x + 1),
                                    neighbour_y,
                                    neighbour_z,
                                )
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        # Check in which direction the wire is moving
                        if (
                            node_x == neighbour_x
                            and node_y - 1 == neighbour_y
                            and node_z == neighbour_z
                            and counter > 1
                        ):
                            # Check if an intersection can be made
                            if self.is_valid(
                                neighbour_x, (neighbour_y - 1), neighbour_z
                            ):
                                # Route is appended and intersection is counted
                                after_intersection = (
                                    neighbour_x,
                                    (neighbour_y - 1),
                                    neighbour_z,
                                )
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        # Check in which direction the wire is moving
                        if (
                            node_x == neighbour_x
                            and node_y + 1 == neighbour_y
                            and node_z == neighbour_z
                            and counter > 1
                        ):
                            # Check if an intersection can be made
                            if self.is_valid(
                                neighbour_x, (neighbour_y + 1), neighbour_z
                            ):
                                # Route is appended and intersection is counted
                                after_intersection = (
                                    neighbour_x,
                                    (neighbour_y + 1),
                                    neighbour_z,
                                )
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        # Check in which direction the wire is moving
                        if (
                            node_x == neighbour_x
                            and node_y == neighbour_y
                            and node_z - 1 == neighbour_z
                            and counter > 1
                        ):
                            # Check if an intersection can be made
                            if self.is_valid(
                                neighbour_x, neighbour_y, (neighbour_z - 1)
                            ):
                                # Route is appended and intersection is counted
                                after_intersection = (
                                    neighbour_x,
                                    neighbour_y,
                                    (neighbour_z - 1),
                                )
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        # Check in which direction the wire is moving
                        if (
                            node_x == neighbour_x
                            and node_y == neighbour_y
                            and node_z + 1 == neighbour_z
                            and counter > 1
                        ):
                            # Check if an intersection can be made
                            if self.is_valid(
                                neighbour_x, neighbour_y, (neighbour_z - 1)
                            ):
                                # Route is appended and intersection is counted
                                after_intersection = (
                                    neighbour_x,
                                    neighbour_y,
                                    (neighbour_z + 1),
                                )
                                new_route = list(route)
                                new_route.append(neighbour)
                                new_route.append(after_intersection)
                                queue.append(new_route)
                                intersections += 1

                        else:
                            # If no intersection can be made, node is appended to explored list
                            explored.append(node)

                    else:
                        # If step is valid, the route is appended
                        new_route = list(route)
                        new_route.append(neighbour)
                        queue.append(new_route)

                    # Check if the end point has been reached
                    if self.end_point(neighbour_x, neighbour_y, neighbour_z):
                        # The score for the solution is calculated
                        wire_count = len(new_route) - 1
                        intersection_count = intersections
                        score_new_route = wire_count + (300 * intersection_count)
                        solutions_counter += 1

                        # Score checked if it is lower than the best solution
                        if score_new_route < score_best_solution:
                            # New route becomes the best solution route
                            best_solution_route = new_route
                            score_best_solution = score_new_route

                # Node is added to explored list
                intersections = 0
                explored.append(node)

            # Check if 5 solutions have been found
            if solutions_counter == 5:
                break

        # Checks if a solution has been found
        if solutions_counter >= 1:
            # The wire count is calculated for the best route
            wire_count = (len(best_solution_route) - 1)

            # Write down the route with "1" expect the gates, that must stay X
            for coord in best_solution_route:
                coord_x = coord[0]
                coord_y = coord[1]
                coord_z = coord[2]

                # Check if coord is the end_gate
                if (
                    coord_x == self.end_gate_x
                    and coord_y == self.end_gate_y
                    and coord_z == 0
                ):
                    continue
                # Check if coord is the start_gate
                elif (
                    coord_x == self.start_gate_x
                    and coord_y == self.start_gate_y
                    and coord_z == 0
                ):
                    continue
                # Writes down the route with "1"
                else:
                    self.board[coord_z][coord_y][coord_x] = "1"

            return best_solution_route, wire_count, self.board

        # If no solution is found, returns crashed
        else:
            return "crashed"

    def find_neighbours(self, node):
        """
        checks for the neighbours of a node and if they are inside the board.

        Args:
            node (tuple): tuple with coordinates x, y and z

        Returns:
            list of tuples, where the tuples are the coordinates of the neighbours of the node

        """

        x, y, z = node[0]

        # Neighbours are calculated
        neighbours = [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]
        neighbour_counter = 0

        # Neighbours are checked if they are on the board
        while neighbour_counter < len(neighbours):

            for (i, j, k,) in neighbours:
                # Each coordinate is checked
                if (
                    (self.size <= j or j <= 0)
                    or (self.size <= i or i <= 0)
                    or (self.size < k or k < -self.size)
                ):
                    neighbours[neighbour_counter] = None
                    neighbour_counter += 1
                else:
                    neighbour_counter += 1
                    continue

        return [i for i in neighbours if i is not None]

    def score_calculator(self, wire_count, intersections):
        """
            calculates the cost of a connection to validate if a connection is cheaper.

            Args:
                wire count (int): integer that gives the wire count

            Returns:
                integer, the cost value of a solution

        """

        cost = wire_count + 300 * intersections

        return cost
