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
        print(netlist_distance)

    sorted_netlist = dict(sorted(netlist_distance.items(), key=lambda item: item[1]))

    print(sorted_netlist)
    print(sorted_netlist.keys())

    return sorted_netlist.keys()


if __name__ == '__main__':
    gatesfilepath = "data/chip_0/print_0.csv"
    netlistpath = "data/chip_0/netlist_1.csv"

    board_obj = Grid(gatesfilepath, netlistpath)
    sorting(board_obj.netlist, board_obj.gates_dict)