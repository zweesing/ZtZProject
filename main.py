from code.classes.grid import Grid, writetofile
from code.algorithms.find import Pathfind

# make the grid in a size that fits all the gates, and add the gates
gatesfilepath = "data/gates_and_netlists1/print_0.csv"
netlistpath = "data/gates_and_netlists1/netlist_1.csv"
board_obj = Grid(gatesfilepath, netlistpath)
print(board_obj)
board = board_obj.get_board()

# read out all connections that need to be made

print("netlist:")
print(board_obj.netlist)

# now we can use both netlist and gates dict to get all the start and end points
# and have pathfinder solve those
routes = []
totalwirecount = 0

# solve every connection with pathfinder
for connection in board_obj.netlist:
    start, stop = connection

    start_coord = board_obj.gates_dict[start]
    stop_coord = board_obj.gates_dict[stop]

    path = Pathfind(start_coord, stop_coord, board)
    print()

    route, wire_count, board = path.find()
    routes.append(route)
    totalwirecount += wire_count

    print(path)
    print(route)
    print(wire_count)

writetofile(board_obj.netlist, routes, totalwirecount)
