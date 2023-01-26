#  loop for random
from code.classes.grid import writetofile, Grid
import random
import copy


def looptest(algoritme, gatesfilepath, netlistpath):
    """tests a chosen algoritme until it has a solution to the problem.

    Args:
        algoritme: the algoritme that needs to be tested and is called upon to run.
        gatesfile: path to csv file with gate positions
        netlistfile: path to csv file with connections to be made
        solution_nr (int): number of the solution, for output file writing

    Returns:
        pathfinder object, list, int: list of tuples containing the route taken and the total wire count needed
        to make the connections.
    """
    crash_counter = 0
    board_obj = Grid(gatesfilepath, netlistpath)
    board_og = board_obj.get_board()

    print("LOOPTEST")
    while True:
        routes = []
        totalwirecount = 0

        board = copy.deepcopy(board_og)

        random.shuffle(board_obj.netlist)

        for connection in board_obj.netlist:
            start, stop = connection

            start_coord = board_obj.gates_dict[start]
            stop_coord = board_obj.gates_dict[stop]

            path = algoritme(start_coord, stop_coord, board)
            print()

            returns = path.find()
            if returns == "crashed":
                crash_counter += 1
                print(crash_counter)

                break

            route, wire_count, board = returns
            routes.append(route)
            totalwirecount += wire_count

        if returns != "crashed":
            writetofile(board_obj.netlist, routes, totalwirecount)

            return path, routes, totalwirecount, crash_counter
