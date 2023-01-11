from pathfinder import Pathfinder
import csv


def read_gates(path):
    """read in the gates from a csv file, and save to dictionary. Also checks what the biggest position is
    where a gate is placed, to later determine the board size. currently returns one maxcoord, for a square board.

    Args:
        path (string): path to csv file containing the gate positions

    Returns:
        dictionary, maxcoord: the dictioinary with the gate name and coordinates, and the max coordinate to determine grid size
    """
    gatesdict = {}
    max_coord = 0

    with open(gatesfilepath) as gatesfile:
        header = gatesfile.readline()
        lines = gatesfile.readlines()

        for line in lines:
            line = line.strip().split(",")
            # csv contains name of gate, then x then y coordinate
            gatesdict[line[0]] = (int(line[1]), int(line[2]))

            # check for max coordinate
            if int(line[1]) > max_coord:
                max_coord = int(line[1])

            if int(line[2]) > max_coord:
                max_coord = int(line[2])

    return gatesdict, max_coord


def read_netlist(path):
    """read a csv file containing the netlists, the connections that need to be made between gates.

    Args:
        path (str): path to the csv file

    Returns:
        list: list containing tuples (startgate, endgate)
    """
    netlist = []
    with open(path) as gatesfile:
        header = gatesfile.readline()
        lines = gatesfile.readlines()

        for line in lines:
            line = line.strip().split(",")
            netlist.append(tuple(line))

    return netlist


# now only squares. need to test x and y seperatly to also make rectangles if needed.


class Grid:
    def __init__(self, column, row, gates):
        """create a board (nested list) of size row x column.

        Args:
            column (int): width of board
            row (int): height of board
            gates (dict): name and coordinates of the gates on the board
        """
        self.column = column
        self.row = row
        self.board = []
        self.gates_dict = gates
        self.make_board()

    def make_board(self):
        """make the board based on input giving to instance.
        Also calls place_gate to fill the board.
        """
        # Function makes a board based on the column and row input of the user
        for row in range(self.row):
            self.board.append([])
            for width in range(self.column):
                self.board[row].append("0")

        # add gates
        for gate in self.gates_dict:
            self.place_gate(self.gates_dict[gate])

    def get_board(self):
        """get the board created.

        Returns:
            list: nested list of the board
        """
        return self.board

    def place_gate(self, coords):
        """Places a gate at the coordinates given by the user.
        Because of nested lists it is important to ask first row then column.

        Args:
            coords (tuple): x,y position of the gate
        """

        #
        column, row = coords
        self.board[row][column] = "X"

    def __repr__(self):
        """representation of the board for visualising.

        Returns:
            str: printable representation
        """
        return "\n".join([" ".join(row) for row in self.board])


# Make a dictionary at the end were net list(route) is linked to the actual found route.


def writetofile(netlist, routes, wirecount):
    """write the results to a csv file (currently "output.csv"). The file contains netlist and corresponding route,
    as well as the total wire count to calculate costs.

    Args:
        netlist (list): the netlist with tuples of the gate connections
        routes (list): list containing the routes taken for every connection
        wirecount (int): total number of wires used
    """
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(("net", "wires"))

        for i in range(len(routes)):
            writer.writerow((netlist[i], routes[i]))

        writer.writerow(("wirecount", wirecount))


if __name__ == "__main__":

    # make the grid in a size that fits all the gates, and add the gates
    gatesfilepath = "gates_and_netlists/print_0.csv"
    dict, max_coord = read_gates(gatesfilepath)
    size = max_coord + 1
    board_obj = Grid(size, size, dict)
    print(board_obj)
    board = board_obj.get_board()

    # read out all connections that need to be made
    netlistpath = "gates_and_netlists/netlist_1.csv"
    netlist = read_netlist(netlistpath)
    print("netlist:")
    print(netlist)

    # now we can use both netlist and gates dict to get all the start and end points
    # and have pathfinder solve those
    routes = []
    totalwirecount = 0

    # solve every connection with pathfinder
    for connection in netlist:
        start, stop = connection

        start_coord = dict[start]
        stop_coord = dict[stop]

        path = Pathfinder(start_coord, stop_coord, board)
        print()

        route, wire_count, board = path.find()
        routes.append(route)
        totalwirecount += wire_count

        print(path)
        print(route)
        print(wire_count)

    writetofile(netlist, routes, totalwirecount)
