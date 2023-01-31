#  loop for random
from code.classes.grid import writetofile, Grid
from code.classes.sortingnetlist import sorting
import random
import copy
import time


def looptest(algoritme, gatesfilepath, netlistpath, sorted=False):
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
    connection_counter = 0
    board_obj = Grid(gatesfilepath, netlistpath)
    board_og = board_obj.get_board()

    if sorted:
        sorted_lists = sorting(board_obj.netlist, board_obj.gates_dict)

    print("LOOPTEST")

    # timings

    while True:
        starttime_single_solution = time.time()

        routes = []
        totalwirecount = 0
        total_intersections = 0

        board = copy.deepcopy(board_og)

        # if shuffle
        if not sorted:
            random.shuffle(board_obj.netlist)

            for connection in board_obj.netlist:
                start, stop = connection

                start_coord = board_obj.gates_dict[start]
                stop_coord = board_obj.gates_dict[stop]

                path = algoritme(start_coord, stop_coord, board, board_obj.size)

                returns = path.find()

                connection_counter += 1

                if returns == "crashed":
                    crash_counter += 1
                    print(
                        f"crashcounter: {crash_counter}, crashed at: {connection_counter}"
                    )
                    connection_counter = 0

                    break

                route, wire_count, board = returns
                routes.append(route)
                totalwirecount += wire_count
        # if sorted option
        else:

            for sorted_list in sorted_lists:
                for connection in sorted_list:

                    start, stop = connection

                    start_coord = board_obj.gates_dict[start]
                    stop_coord = board_obj.gates_dict[stop]

                    path = algoritme(start_coord, stop_coord, board, board_obj.size)

                    returns = path.find()

                    connection_counter += 1

                    if returns != "crashed":
                        route, wire_count, board = returns
                        routes.append(route)
                        totalwirecount += wire_count

                    if returns == "crashed":
                        crash_counter += 1
                        print(
                            f"crashcounter: {crash_counter}, crashed at: {connection_counter}"
                        )
                        connection_counter = 0

                        break
                if returns == "crashed":
                    break

        if returns != "crashed":
            writetofile(board_obj.netlist, routes, totalwirecount)
            endtime_single_solution = time.time()
            single_runtime = endtime_single_solution - starttime_single_solution

            return (
                path,
                routes,
                totalwirecount,
                crash_counter,
                board_obj.netlist,
                single_runtime,
            )
