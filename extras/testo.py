import csv

gatesdict = {}
gatesfilepath = "gates_and_netlists/print_0.csv"
with open(gatesfilepath) as gatesfile:
    header = gatesfile.readline()
    lines = gatesfile.readlines()

    for line in lines:
        line = line.strip().split(",")
        gatesdict[line[0]] = (int(line[1]), int(line[2]))

    print(gatesdict)
