from code.algorithms.constructive import Constructive
from code.algorithms.greedy import Pathfind
from code.classes.looptester import looptest
from code.visualisation.visualisation3D import visualize
from code.algorithms.random import Pathfindrandom
from code.classes.helper_funcs import (
    intersect_count,
    cost_calc,
    writetofile,
    writecoststofile,
)
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
    help="Choose between \"greedy\", \"breadth\" or \"breadthext\" for respectively a greedy/random algoritm, a breadth first  or an extended breadth first algoritm",
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
    help="Choose a netlist in range 1-3, default netlist is 1",
)
parser.add_argument(
    "--iteration",
    "-i",
    type=int,
    help="Choose the amount of solutions you want returned",
    default = 1,
)
parser.add_argument(
    "--sorted",
    "-s",
    type=bool,
    help="Choose between sorted False or True, if false it wil be random. Default is False. ",
    default = False,
)

# Unpack arguments
args = parser.parse_args()
chip = args.chip
netlistnr = args.netlist
algorithm = args.algorithm

# Load correct gates file and correct netlist file
gatesfilepath = f"data/chip_{chip}/print_{chip}.csv"
netlistpath = f"data/chip_{chip}/netlist_{3 * chip + netlistnr}.csv"

savefolder = f"{algorithm}_chip{chip}_netlist{3 * chip + netlistnr}"

gates, _ = Grid.read_gates(1, gatesfilepath)
cost_list = []
# Iterate the correct amount of times, during iteration run the chosen algoritm until it finds a solution
for i in range(args.iteration):
    if algorithm == "greedy":
        results = looptest(Pathfind, gatesfilepath, netlistpath, sorted=True)
    if algorithm == "breadth":
        results = looptest(Constructive, gatesfilepath, netlistpath, sorted=True)
    if algorithm == "random":
        results = looptest(Pathfindrandom, gatesfilepath, netlistpath, sorted=True)
    path, routes, totalwirecount, crash_counter, netlist = results
    writetofile(
        netlist,
        routes,
        totalwirecount,
        savefolder,
        i,
    )

    cost = cost_calc(routes, gates, totalwirecount)
    cost_list.append(cost)

print(cost_list)
writecoststofile(cost_list, savefolder)

# Visualize the outputfile
visualize("output.csv", gatesfilepath)
