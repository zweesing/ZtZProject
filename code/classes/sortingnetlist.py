import math
from code.classes.grid import Grid


def sorting(netlist, gates_dict):
    """sorts a given netlist, based on the distance between the gates.

        Args:
            gates_dict: list with gate positions
            netlist: list with connections to be made

        Returns:
            list of compartmentalized sorted netlist.
    """
    netlist_distance = {}

    for connection in netlist:
        start, stop = connection

        start_coord = gates_dict[start]
        stop_coord = gates_dict[stop]

        distance = math.dist(start_coord, stop_coord)

        netlist_distance[connection] = distance

    sorted_netlist = dict(sorted(netlist_distance.items(), key=lambda item: item[1]))
    sorted_netlist_keys = sorted_netlist.keys()
    first_half_sorted_netlist = []

    halfs = int(len(sorted_netlist_keys) / 2)
    for i in halfs:
        first_half_sorted_netlist = sorted_netlist_keys.pop(0)

    second_half_sorted_netlist = sorted_netlist_keys

    return [first_half_sorted_netlist, second_half_sorted_netlist]


