#  loop for random
from code.classes.grid import writetofile, Grid


def looptest(algoritme, gatesfilepath, netlistpath):
    crash_counter = 0

    print("LOOPTEST")
    while True:
        routes = []
        totalwirecount = 0

        board_obj = Grid(gatesfilepath, netlistpath)
        board = board_obj.get_board()

        for connection in board_obj.netlist:
            start, stop = connection

            start_coord = board_obj.gates_dict[start]
            stop_coord = board_obj.gates_dict[stop]

            path = algoritme(start_coord, stop_coord, board)
            print()

            returns = path.find()
            if returns == "crashed":
                crash_counter += 1
                print(crash_counter)

                break

            route, wire_count, board = returns
            routes.append(route)
            totalwirecount += wire_count

        if returns != "crashed":
            writetofile(board_obj.netlist, routes, totalwirecount)
            return path, route, totalwirecount
