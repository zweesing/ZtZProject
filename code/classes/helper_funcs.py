import csv


def intersect_count(routes, gates):

    # make the coords 3d
    gates_list2d = list(gates.values())
    gates_list = []
    for gate in gates_list2d:
        x, y = gate
        gates_list.append((x, y, 0))

    print(gates_list)
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
    intersections = intersect_count(routes, gates)
    cost = wirecount + 300 * intersections
    return cost

def writetofile(netlist, routes, wirecount, path, nr):
    """write the results to a csv file (currently "output.csv"). The file contains netlist and corresponding route,
    as well as the total wire count to calculate costs.

    Args:
        netlist (list): the netlist with tuples of the gate connections
        routes (list): list containing the routes taken for every connection
        wirecount (int): total number of wires used
    """
    with open(f"results/{path}/output{nr}.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(("net", "wires"))

        for i in range(len(routes)):
            writer.writerow((netlist[i], routes[i]))

        writer.writerow(("wirecount", wirecount))
