import matplotlib.pyplot as plt
from code.classes.grid import Grid


def visualize(outputfile, gatesfilepath):

    with open(outputfile) as outputfile:
        header = outputfile.readline()
        lines = outputfile.readlines()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title("Chips and Circuits")

        maxz = [] 
        array_z = []

        for i in range(len(lines) - 1):
            line = lines[i]
            splits = line.strip().split("\"")
            route = splits[3]  
            route = route.split(',')

            route_list = []
            x = []
            y = []
            z = []

            for element in route:
                number = int(element.strip('( )[]'))
                route_list.append(number)

            for i in range(0, len(route_list), 3):
                x.append(route_list[i])
                y.append(route_list[i+1])
                z.append(route_list[i+2])

            maxz.append(max(z))
        
            ax.plot(x,y,z)
       
        for i in range(max(maxz) + 1):
            array_z.append(i) 

        ax.set_zlim(0, max(maxz))
        ax.set_zticks(array_z)

    gatesdict, _ = Grid.read_gates(1, gatesfilepath)
    keys = gatesdict.keys()
    for key in keys:
        x, y = gatesdict[key]
        ax.text(x, y, 0, key, color="black", fontweight="bold", bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))

    plt.show()



   