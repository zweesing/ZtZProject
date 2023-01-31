from code.algorithms.constructive import Constructive
from code.algorithms.greedy import Pathfind
from code.classes.looptester import looptest
from code.visualisation.visualisation3D import visualize
from code.classes.helper_funcs import intersect_count, cost_calc, writetofile
from code.classes.grid import Grid
import argparse
import sys

"""
Runs the tests of a chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

parser = argparse.ArgumentParser()
parser.add_argument("--algorithm", "-a", help="Choose between greedy and breadth for respectively a greedy/random algoritm or a breadth first algoritm")
parser.add_argument("--chip", "-c", type=int, default=0, help="Choose a chip in range 0-2")
parser.add_argument("--netlist", "-n", type=int, default=1, help="Choose a chip in range 1-3")
parser.add_argument("--iteration", "-i", type=int, help="Choose the amount of solutions you want returned")
args = parser.parse_args()

chip = args.chip
netlist = args.netlist
algorithm = args.algorithm

gatesfilepath = f"data/chip_{chip}/print_{chip}.csv"
netlistpath = f"data/chip_{chip}/netlist_{3 * chip + netlist}.csv"


for i in range(args.iteration):
    if algorithm == "greedy":
        results = looptest(Pathfind, gatesfilepath, netlistpath)
    if algorithm == "breadth":
        results = looptest(Constructive, gatesfilepath, netlistpath)
    path, routes, totalwirecount, crash_counter, netlist = results
    writetofile(netlist, routes, totalwirecount, "greedyrandom_chip1_netlist4", i)


print(path)
print(routes)
print(totalwirecount)
# print(total_counter)

# stupid way of reading gates in, needed for calculation
gates, _ = Grid.read_gates(1, gatesfilepath)

# calculate intersections
intersections = intersect_count(routes, gates)

cost = cost_calc(routes, gates, totalwirecount)
print(f"costs: {cost}, intersections: {intersections}")
visualize("output.csv", gatesfilepath)
