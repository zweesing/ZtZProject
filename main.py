from code.algorithms.random import Pathfindrandom
from code.algorithms.fixer import Pathfind_GR
from code.algorithms.constructive import Constructive
from code.classes.looptester import looptest
from code.visualisation.visualisation3D import visualize
from code.classes.helper_funcs import intersect_count
from code.classes.grid import Grid

"""
Runs the tests of a chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

gatesfilepath = "data/chip_0/print_0.csv"
netlistpath = "data/chip_0/netlist_1.csv"
total_counter = 0
# get 50 results and see how long that took

results = looptest(Pathfind_GR, gatesfilepath, netlistpath)

path, routes, totalwirecount, crash_counter = results
total_counter += crash_counter


print(path)
print(routes)
print(totalwirecount)
print(total_counter)

# stupid way of reading gates in, needed for calculation
gates, _ = Grid.read_gates(1, gatesfilepath)

# calculate intersections
intersections = intersect_count(routes, gates)

cost = totalwirecount + 300 * intersections
print(f"costs: {cost}, intersections: {intersections}")
visualize("output.csv", gatesfilepath)
