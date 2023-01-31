from code.algorithms.random import Pathfindrandom
from code.algorithms.fixer import Pathfind_GR
from code.algorithms.constructive import Constructive
from code.algorithms.greedy import Pathfind
from code.classes.looptester import looptest, looptestgreedy
from code.visualisation.visualisation3D import visualize
from code.classes.helper_funcs import intersect_count, cost_calc, writetofile
from code.classes.grid import Grid

"""
Runs the tests of a chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

chip = 0
netlist = 2
gatesfilepath = f"data/chip_{chip}/print_{chip}.csv"
netlistpath = f"data/chip_{chip}/netlist_{3 * chip + netlist}.csv"


for i in range(100):
    results = looptestgreedy(Pathfind, gatesfilepath, netlistpath)
    path, routes, totalwirecount, crash_counter, netlist = results
    writetofile(netlist, routes, totalwirecount, "greedyrandom_chip1_netlist4", i)


# print(path)
# print(routes)
# print(totalwirecount)
# print(total_counter)

# stupid way of reading gates in, needed for calculation
gates, _ = Grid.read_gates(1, gatesfilepath)

# calculate intersections
intersections = intersect_count(routes, gates)

cost = cost_calc(routes, gates, totalwirecount)
print(f"costs: {cost}, intersections: {intersections}")
visualize("output.csv", gatesfilepath)
