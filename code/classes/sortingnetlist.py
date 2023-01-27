import math
from code.classes.grid import Grid


def sorting(netlist, gates_dict):
    netlist_distance = {}

    for connection in netlist:
        start, stop = connection

        start_coord = gates_dict[start]
        stop_coord = gates_dict[stop]

        distance = math.dist(start_coord, stop_coord)

        netlist_distance[connection] = distance

    sorted_netlist = dict(sorted(netlist_distance.items(), key=lambda item: item[1]))

    return sorted_netlist.keys()


