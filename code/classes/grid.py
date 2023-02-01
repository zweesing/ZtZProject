import csv


class Grid:
    def __init__(self, gatesfile, netlistfile):
        """
        Creates a board and places the gates specified in gatesfile (csv) on it,
        such that there is a border of size one around the gates on the edge.

        Args:
            gatesfile: path to csv file with gate positions
            netlistfile: path to csv file with connections to be made
        """
        
        self.board = []

        self.gates_dict, max_coord = self.read_gates(gatesfile)

        self.netlist = self.read_netlist(netlistfile)

        self.size = max_coord + 2

        self.make_board()

    def read_gates(self, path):
        """
        Reads in the gates from a csv file, and saves to a dictionary. Also checks what the biggest position is
        where a gate is placed, to later determine the board size. Returns one maxcoord, for a square board.

        Args:
            Path (string): path to csv file containing the gate positions

        Returns:
            Dictionary, int: the dictioinary with the gate name and coordinates, and the max coordinate to determine grid size
        """

        gatesdict = {}
        max_coord = 0

        with open(path) as gatesfile:
            header = gatesfile.readline()
            lines = gatesfile.readlines()

            for line in lines:
                line = line.strip().split(",")
                
                # Csv contains name of gate, then x then y coordinate
                gatesdict[line[0]] = (int(line[1]), int(line[2]))

                # Check for max coordinate
                if int(line[1]) > max_coord:
                    max_coord = int(line[1])

                if int(line[2]) > max_coord:
                    max_coord = int(line[2])

        return gatesdict, max_coord

    def read_netlist(self, path):
        """
        Reads a csv file containing the netlists, the connections that need to be made between gates.

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

    def make_board(self):
        """
        Makes the board with a size based on the maximum coordinates of the gates in the board. 
        The length and width are so that the gates fit in with an edge around them, and the height is double the size of the board.
        Also calls place_gate to fill the board.
        """

        rows = self.size
        columns = self.size
        levels = self.size * 2

        # Function makes a board based on the size
        for level in range(levels):
            self.board.append([])
            for row in range(rows):
                self.board[level].append([])
                for width in range(columns):
                    self.board[level][row].append("0")

        # Add gates to board
        for gate in self.gates_dict:
            self.place_gate(self.gates_dict[gate])

    def get_board(self):
        """
        Get the board created.

        Returns:
            list: nested list of the board
        """

        return self.board

    def place_gate(self, coords):
        """
        Places a gate at the correct coordinates found in the file.

        Args:
            coords (tuple): x,y position of the gate, z coordinate is always 0
        """

        column, row = coords
        self.board[0][row][column] = "X"


def writetofile(netlist, routes, wirecount):
    """
    Write the results to a csv file (currently "output.csv"). The file contains netlist and corresponding route,
    as well as the total wire count to calculate costs.

    Args:
        netlist (list): the netlist with tuples of the gate connections
        routes (list): list containing the routes taken for every connection
        wirecount (int): total number of wires used
    """

    with open(f"output.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(("net", "wires"))

        for i in range(len(routes)):
            writer.writerow((netlist[i], routes[i]))

        writer.writerow(("wirecount", wirecount))
