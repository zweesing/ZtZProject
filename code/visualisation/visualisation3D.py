import matplotlib.pyplot as plt


def visualize(outputfile):

    with open(outputfile) as outputfile:
        header = outputfile.readline()
        lines = outputfile.readlines()

        for i in range(len(lines) - 1):
            line = lines[i]
            splits = line.strip().split("\"")
            route = splits[3]  
            
            list(route)

            # hij geeft met route wel goed aan dat het een lijst is maar hij denkt dat het een lijst is met 1 string erin
            # ik moet dus erachter zien te komen hoe ik die string naar wel een lijst met tuples zie te krijgen

if __name__ == "__main__":
    blip = visualize("output.csv")

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # x = [2,3,3,3,5,7,9,11,9,10]
    # y = [3,5,7,1,2,4,5,9,4,2]
    # z = [1,2,3,4,5,6,7,8,9,10]
    # ax.plot(x,y,z)

    # plt.show()