from code.classes.grid import writetofile, Grid
from code.classes.sortingnetlist import sorting
import random
import copy
import time


def looptest(algoritme, gatesfilepath, netlistpath, sorted=False):
    """
    Tests a chosen algoritme until it has a solution to the problem.

    Args:
        algoritme: the algoritme that needs to be tested and is called upon to run.
        gatesfile: path to csv file with gate positions
        netlistfile: path to csv file with connections to be made
        sorted: bool expression, that by deafault is False

    Returns:
        pathfinder object, list, int, int, list, int: list of tuples containing the route taken, the total wire count
        needed to make the connections, the amount of times crashed, a list of the netlist used and the runtime of a
        single solution.
    """

    crash_counter = 0
    connection_counter = 0
    board_obj = Grid(gatesfilepath, netlistpath)
    board_og = board_obj.get_board()

    # Checks if user wants to run a sorted netlist and then runs sorting function
    if sorted:
        sorted_lists = sorting(board_obj.netlist, board_obj.gates_dict)

    print("LOOPTEST")

    # Keeps running until a solution has been found
    while True:
        starttime_single_solution = time.time()
        routes = []
        totalwirecount = 0
        total_intersections = 0

        board = copy.deepcopy(board_og)

        # If user wants to run shuffled netlist
        if not sorted:
            # Randomizes the netlist
            random.shuffle(board_obj.netlist)

            # Runs the algoritme for each connection
            for connection in board_obj.netlist:
                start, stop = connection

                start_coord = board_obj.gates_dict[start]
                stop_coord = board_obj.gates_dict[stop]

                path = algoritme(start_coord, stop_coord, board, board_obj.size)

                returns = path.find()

                connection_counter += 1

                # If algoritme crashes, break out of for loop and start again from first connection
                if returns == "crashed":
                    crash_counter += 1
                    if crash_counter % 20 == 0:
                        print(
                            f"crashcounter: {crash_counter}, crashed at: {connection_counter}"
                        )
                    connection_counter = 0

                    break

                # If algoritme doesn't break append route and calculate total wire count
                route, wire_count, board = returns
                routes.append(route)
                totalwirecount += wire_count

        # If user wants to run sorted netlist
        else:

            # Runs the first half of the connections first then the second
            for sorted_list in sorted_lists:
                # Randomizes the halved netlist
                random.shuffle(sorted_list)
                # Runs the algoritme for each connection
                for connection in sorted_list:

                    start, stop = connection

                    start_coord = board_obj.gates_dict[start]
                    stop_coord = board_obj.gates_dict[stop]

                    path = algoritme(start_coord, stop_coord, board, board_obj.size)

                    returns = path.find()

                    connection_counter += 1

                    # If algoritme doesn't break append route and calculate total wire count
                    if returns != "crashed":
                        route, wire_count, board = returns
                        routes.append(route)
                        totalwirecount += wire_count

                    # If algorimte crashes, break out of for loop and start again from first connection
                    if returns == "crashed":
                        crash_counter += 1
                        if crash_counter % 20 == 0:
                            print(
                                f"crashcounter: {crash_counter}, crashed at: {connection_counter}"
                            )
                        connection_counter = 0

                        break

                # If algoritme crashed break out of the double for loop
                if returns == "crashed":
                    break

        # If all connections are found return results and make csv file
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
