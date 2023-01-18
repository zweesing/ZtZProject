from code.classes.grid import Grid
from code.algorithms.find import Pathfind
from code.algorithms.baseline import Pathfindrandom
from code.classes.looptester import looptest


# make the grid in a size that fits all the gates, and add the gates
gatesfilepath = "data/gates_and_netlists1/print_0.csv"
netlistpath = "data/gates_and_netlists1/netlist_1.csv"

results = looptest(Pathfindrandom, gatesfilepath, netlistpath)
path, route, totalwirecount = results

print(path)
print(route)
print(totalwirecount)
