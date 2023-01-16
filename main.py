from code.classes.grid import Grid, read_gates, read_netlist, writetofile
from code.algorithms.find import Pathfind

# make the grid in a size that fits all the gates, and add the gates
gatesfilepath = "data/gates_and_netlists1/print_0.csv"
dict, max_coord = read_gates(gatesfilepath)
size = max_coord + 1
board_obj = Grid(size, size, dict)
print(board_obj)
board = board_obj.get_board()

# read out all connections that need to be made
netlistpath = "data/gates_and_netlists1/netlist_1.csv"
netlist = read_netlist(netlistpath)
print("netlist:")
print(netlist)

# now we can use both netlist and gates dict to get all the start and end points
# and have pathfinder solve those
routes = []
totalwirecount = 0

# solve every connection with pathfinder
for connection in netlist:
    start, stop = connection

    start_coord = dict[start]
    stop_coord = dict[stop]

    path = Pathfind(start_coord, stop_coord, board)
    print()

    route, wire_count, board = path.find()
    routes.append(route)
    totalwirecount += wire_count

    print(path)
    print(route)
    print(wire_count)

writetofile(netlist, routes, totalwirecount)
