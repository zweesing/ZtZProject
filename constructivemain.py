from code.algorithms.constructive import Constructive
from code.classes.helper_funcs import writetofile
from code.classes.looptester import looptest
from code.visualisation.visualisation3D import visualize

"""
Runs the tests of a chosen algoritme. With the chosen netlist and gate csv files. 

It returns the last board, last route and the total wire count. In looptest an output file is also created showing the 
data in a csv file.
"""

gatesfilepath = "data/chip_1/print_1.csv"
netlistpath = "data/chip_1/netlist_4.csv"
total_counter = 0
# get 50 results and see how long that took
for i in range (5):
    results = looptest(Constructive, gatesfilepath, netlistpath)
    path, routes, totalwirecount, crash_counter, netlist = results
    writetofile(netlist, routes, totalwirecount, 'constructive_chip1_netlist4', i )

total_counter += crash_counter



print(path)
print(routes)
print(totalwirecount)
print(total_counter)

visualize("output.csv", gatesfilepath)
