import csv


# now only squares. need to test x and y seperatly to also make rectangles if needed.


class Grid:
    def __init__(self, gatesfile, netlistfile):
        """create a board and places the gates specified in gatesfile (csv) on it,
        such that there is a border of size one around the gates on the edge.

        Args:
            gatesfile: path to csv file with gate positions
            netlistfile: path to csv file with connections to be made
        """
        # gates is now file path
        self.board = []

        self.gates_dict, max_coord = self.read_gates(gatesfile)

        self.netlist = self.read_netlist(netlistfile)

        self.make_board(max_coord)

    def read_gates(self, path):
        """read in the gates from a csv file, and save to dictionary. Also checks what the biggest position is
        where a gate is placed, to later determine the board size. currently returns one maxcoord, for a square board.

        Args:
            path (string): path to csv file containing the gate positions

        Returns:
            dictionary, int: the dictioinary with the gate name and coordinates, and the max coordinate to determine grid size
        """
        gatesdict = {}
        max_coord = 0

        with open(path) as gatesfile:
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

    def read_netlist(self, path):
        """read a csv file containing the netlists, the connections that need to be made between gates.

        Args:
            path (str): path to the csv file with connections

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

    def make_board(self, size):
        """make the board based on input giving to instance.
        The length and width are so that the gates fit in with an edge around them, and the height is for now just half of that.
        Also calls place_gate to fill the board.
        """
        rows = size + 2
        columns = size + 2
        levels = size / 2
        # Function makes a board based on the column and row input of the user
        for level in range(levels):
            self.board.append([])
            for row in range(rows):
                self.board[level].append([])
                for width in range(columns):
                    self.board[level][row].append("0")

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
        self.board[0][row][column] = "X"

    def __repr__(self):
        """representation of the board for visualising.

        Returns:
            str: printable representation
        """
        return "\n".join([" ".join(row) for row in self.board])


# Make a dictionary at the end were net list(route) is linked to the actual found route.


def writetofile(netlist, routes, wirecount, number):
    """write the results to a csv file (currently "output.csv"). The file contains netlist and corresponding route,
    as well as the total wire count to calculate costs.

    Args:
        netlist (list): the netlist with tuples of the gate connections
        routes (list): list containing the routes taken for every connection
        wirecount (int): total number of wires used
    """
    with open(f"solutions/output_{number}.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(("net", "wires"))

        for i in range(len(routes)):
            writer.writerow((netlist[i], routes[i]))

        writer.writerow(("wirecount", wirecount))
