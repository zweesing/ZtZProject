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

    # Calculates the distance for each connection given in a netlist
    for connection in netlist:
        start, stop = connection

        start_coord = gates_dict[start]
        stop_coord = gates_dict[stop]

        distance = math.dist(start_coord, stop_coord)

        netlist_distance[connection] = distance

    # The dictionary is sorted based on the distance
    sorted_netlist = dict(sorted(netlist_distance.items(), key=lambda item: item[1]))

    # A list is made sorted based on the distance
    sorted_netlist_keys = list(sorted_netlist.keys())

    # The amount of connections is calculated and divided by 2
    first_half_sorted_netlist = []
    halfs = int(len(sorted_netlist_keys) / 2)

    # A list is made of the first half of the connections from the sorted list
    for i in range(halfs):
        first_half_sorted_netlist.append(sorted_netlist_keys.pop(0))

    # The second half is put in a second list
    second_half_sorted_netlist = sorted_netlist_keys

    return [first_half_sorted_netlist, second_half_sorted_netlist]


