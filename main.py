from code.algorithms.baseline import Pathfindrandom
from code.classes.looptester import looptest
from code.visualisation.visualisation import visualize

"""
Runs the tests of an chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

gatesfilepath = "data/chip_2/print_2.csv"
netlistpath = "data/chip_2/netlist_7.csv"

results = looptest(Pathfindrandom, gatesfilepath, netlistpath)
path, routes, totalwirecount = results

print(path)
print(routes)
print(totalwirecount)

visualize(routes, gatesfilepath)
