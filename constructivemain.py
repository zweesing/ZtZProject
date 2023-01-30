from code.algorithms.constructive import Constructive
from code.classes.looptester import looptest
from code.visualisation.visualisation3D import visualize

"""
Runs the tests of a chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

gatesfilepath = "data/chip_0/print_0.csv"
netlistpath = "data/chip_0/netlist_3.csv"
total_counter = 0
# get 50 results and see how long that took
results = looptest(Constructive, gatesfilepath, netlistpath)


path, routes, totalwirecount, crash_counter, raar_getal = results
total_counter += crash_counter



print(path)
print(routes)
print(totalwirecount)
print(total_counter)

visualize("output.csv", gatesfilepath)
