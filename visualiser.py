from code.visualisation.visualisation3D import visualize

chip = 1

gatesfilepath = f"data/chip_{chip}/print_{chip}.csv"
visualize("results\greedy_sorted_chip1_netlist5\output8.csv", gatesfilepath)
