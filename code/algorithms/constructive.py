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
        counter = 0

        # implementations of depth and or breth search for determining route. Implement 3D part.
        while queue:
            route = queue.pop(0)
            print(route)
            if counter > 0:
                node = [route[-1]]
            else:
                node = route[-1]

            counter += 1
            # print(node)

            if node not in explored:
                neighbours = self.find_neighbours(node)
                print(neighbours)

                for neighbour in neighbours:


                    new_route = list(route)
                    new_route.append(neighbour)
                    queue.append(new_route)

                    neighbour_x = neighbour[0]
                    neighbour_y = neighbour[1]
                    print(neighbour_y, neighbour_x)
                    print("hierna eind coords")
                    print(self.end_gate_y, self.end_gate_x)

                    #check if it is end_point does not work
                    if neighbour_x == self.end_gate_x and neighbour_y == self.end_gate_y:
                        print('hier')
                        print('moet je zijn')
                        print(new_route)
                        return new_route

                explored.append(node)
        print("hier niet")
        return "crashed"

    def find_neighbours(self, node):
        x, y = node[0]
        print(x, y)

        neighbours = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)
        ]
        counter = 0
        while counter < len(neighbours):

            for i, j, in neighbours:
                # print(i)
                # print(j)
                # print(counter)
                # get size from grid board instead of static 7.
                if (7 < j or j < 0) or (7 < i or i < 0):
                    neighbours[counter] = None
                    # print(neighbours)
                    counter += 1
                else:
                    counter += 1
                    continue

        return[i for i in neighbours if i is not None]


if __name__ == '__main__':
    gatesfilepath = "data/chip_0/print_0.csv"
    netlistpath = "data/chip_0/netlist_1.csv"
    results = looptest(Constructive, gatesfilepath, netlistpath)
