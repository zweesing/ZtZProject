from code.algorithms.greedy import Pathfind
from code.classes.looptester import looptest
from code.visualisation.visualisation import visualize

"""
Runs the tests of a chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

gatesfilepath = "data/chip_0/print_0.csv"
netlistpath = "data/chip_0/netlist_1.csv"
total_counter = 0
# get 50 results and see how long that took
for solution in range(50):
    results = looptest(Pathfind, gatesfilepath, netlistpath, solution)

    path, routes, totalwirecount, crash_counter = results
    total_counter += crash_counter


print(path)
print(routes)
print(totalwirecount)
print(total_counter)

visualize(routes, gatesfilepath)
