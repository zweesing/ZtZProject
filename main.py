from code.algorithms.constructive import Constructive
from code.algorithms.greedy import Pathfind
from code.classes.looptester import looptest
from code.visualisation.visualisation3D import visualize
from code.classes.helper_funcs import intersect_count, cost_calc, writetofile
from code.classes.grid import Grid
import argparse

"""
Runs the tests of a chosen algoritme a chosen amount of times. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest the output files are also created showing the 
data in a csv file.
"""

# Create arguments for algorithm, chip, netlist, iteration
parser = argparse.ArgumentParser()
parser.add_argument(
    "--algorithm",
    "-a",
    help="Choose between greedy and breadth for respectively a greedy/random algoritm or a breadth first algoritm",
)
parser.add_argument(
    "--chip",
    "-c",
    type=int,
    default=0,
    help="Choose a chip in range 0-2, default chip is 0",
)
parser.add_argument(
    "--netlist",
    "-n",
    type=int,
    default=1,
    help="Choose a chip in range 1-3, default netlist is 1",
)
parser.add_argument(
    "--iteration",
    "-i",
    type=int,
    help="Choose the amount of solutions you want returned",
)

# Unpack arguments
args = parser.parse_args()
chip = args.chip
netlist = args.netlist
algorithm = args.algorithm

# Load correct gates file and correct netlist file
gatesfilepath = f"data/chip_{chip}/print_{chip}.csv"
netlistpath = f"data/chip_{chip}/netlist_{3 * chip + netlist}.csv"

# Iterate the correct amount of times, during iteration run the chosen algoritm until it finds a solution
for i in range(args.iteration):
    if algorithm == "greedy":
        results = looptest(Pathfind, gatesfilepath, netlistpath, sorted=True)
    if algorithm == "breadth":
        results = looptest(Constructive, gatesfilepath, netlistpath, sorted=True)
    path, routes, totalwirecount, crash_counter, netlist = results
    writetofile(netlist, routes, totalwirecount, "greedyrandom_chip1_netlist4", i)

print(f"total wire count: {totalwirecount}")

# Read gates for intersection calculator
gates, _ = Grid.read_gates(1, gatesfilepath)

# Calculate the amount of intersections
intersections = intersect_count(routes, gates)

# Calculate and print the total cost of placing the wires
cost = cost_calc(routes, gates, totalwirecount)
print(f"costs: {cost}, intersections: {intersections}")

# Visualize the outputfile
visualize("output.csv", gatesfilepath)
