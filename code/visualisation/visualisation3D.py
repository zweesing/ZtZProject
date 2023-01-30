import matplotlib.pyplot as plt
from code.classes.grid import Grid
import matplotlib.ticker as ticker


def visualize(outputfile, gatesfilepath):
    """ 
    Function to visualise the outputfile in 3D
    """

    # open outputfile and read the lines
    with open(outputfile) as outputfile:
        header = outputfile.readline()
        lines = outputfile.readlines()

        # plot figure and make projections 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # set labels for xyz and title chips and circuits
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title("Chips and Circuits")

        # make empty list to store the max z value of each route
        maxz = []
        minz = []
        
        # empty list to store the ticks of the z axis
        array_z = []

        # iterate over all the lines and strip at the quotation marks. Only save split3: the route. 
        for i in range(len(lines) - 1):
            line = lines[i]
            splits = line.strip().split("\"")
            route = splits[3]  
            route = route.split(',')

            # empty lists to store all the integers in the route and to store all the x y or z coordinates
            route_list = []
            x = []
            y = []
            z = []

            # append the strings from the outputfile as integers to the route list
            for element in route:
                number = int(element.strip('( )[]'))
                route_list.append(number)

            # append the x y and z coordinates from the routelist to the correct xyz list
            for i in range(0, len(route_list), 3):
                x.append(route_list[i])
                y.append(route_list[i+1])
                z.append(route_list[i+2])

            # append the max z coordinate from each route
            maxz.append(max(z))
            minz.append(min(z))

            # plot the route
            ax.plot(x,y,z)
       
        # create correct ticks for the z axis
        for i in range(min(minz), max(maxz) + 1):
            array_z.append(i) 
        
        # set correct z ticks
        ax.set_zticks(array_z)
        
        # create tick spacing of 1 for the y and x axis
        tick_spacing = 1
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # create gates in the grid 
    gatesdict, _ = Grid.read_gates(1, gatesfilepath)
    keys = gatesdict.keys()
    for key in keys:
        x, y = gatesdict[key]
        ax.text(x, y, 0, key, color="black", fontweight="bold", bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
    
    # set fontsize to 8
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # show plot
    plt.show()



   