import csv
import os

""" A collection of functions that support mostly main.py, but that are too small to justify giving them their own file. """


def intersect_count(routes, gates):
    """counts the number of intersections that occur in a given solution.
    It does this by checking for overlap in route coordinates, ignoring gate locations.

    Args:
        routes (list): nested list with all routes in the solution
        gates (list): list with all gate locations, in tuples. The gates must be in 2D coordinates.

    Returns:
        int: number of intersections
    """
    # make the coords 3d to compare with route
    gates_list2d = list(gates.values())
    gates_list = []
    for gate in gates_list2d:
        x, y = gate
        gates_list.append((x, y, 0))

    # goes through all routes looking for duplicates.
    seen = set()
    intersect_counter = 0
    for route in routes:
        for coord in route:
            if coord not in seen:
                seen.add(coord)
            elif coord not in gates_list:
                intersect_counter += 1

    return intersect_counter


def cost_calc(routes, gates, wirecount):
    """caculate total cost of a solution, using the intersect_count function

    Args:
        routes (list): nested list with all routes in the solution
        gates (list): list with all gate locations, in tuples. The gates must be in 2D coordinates.
        wirecount (int): number of wires placed in the solution

    Returns:
        int: total cost of the solution
    """
    intersections = intersect_count(routes, gates)
    cost = wirecount + 300 * intersections
    return cost


def writetofile(netlist, routes, wirecount, path, nr):
    """Write the results of a solution to a csv file, as output{nr}.csv in a specified folder within the results directory.
    Folder will be created if it does not exist yet, and if it does, the contents wil be overwritten.
    The file contains netlist and corresponding route, as well as the total wire count to calculate costs. Netlist and routes need to be in the same order.
    Args:
        netlist (list): the netlist with tuples of the gate connections
        routes (list): list containing the routes taken for every connection
        wirecount (int): total number of wires used
        path (str): folder within the results directory where the data should be saved to.
        nr: suffix for the name of output file. Usually the number of the solution within the run.
    """
    # make the directory if it doesnt exist
    if not os.path.exists(f"results/{path}/"):
        os.mkdir(f"results/{path}/")

    # write file
    with open(f"results/{path}/output{nr}.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(("net", "wires"))

        for i in range(len(routes)):
            writer.writerow((netlist[i], routes[i]))

        writer.writerow(("wirecount", wirecount))


def makecostfile(path):
    """Set up the directory and file where the results from a run will be saved to. The directory will be created if it doesn't exist yet.
    The file where the cost and runtime of every solution within a run are written to is initialised with a header.

    Args:
        path (str): folder within the results directory where the data should be saved to.
    """
    if not os.path.exists(f"results/{path}/"):
        os.mkdir(f"results/{path}/")

    with open(f"results/{path}/costs.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(("cost", "runtime"))


def writecoststofile(cost, runtime, path):
    """After finding a a valid solution during a run, this function can be called to write just the cost and runtime of that solution to the costs file to make it easier to find the best result of a run.

    Args:
        cost (int): cost of the solution
        runtime (float): time in seconds that it took to find that solution. Does not include all failed attempts before this solution.
        path (int): folder within results directory where the costs.csv file is made using the makecostfile function.
    """
    with open(f"results/{path}/costs.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow((cost, runtime))
