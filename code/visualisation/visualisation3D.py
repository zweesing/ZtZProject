import matplotlib.pyplot as plt
from code.classes.grid import Grid
import matplotlib.ticker as ticker


def visualize(outputfile, gatesfilepath):
    """ 
    Function to visualise the outputfile in 3D
    """

    # Open outputfile and read the lines
    with open(outputfile) as outputfile:
        header = outputfile.readline()
        lines = outputfile.readlines()

        # Plot figure and make projections 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Set labels for xyz and title chips and circuits
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.set_title("Chips and Circuits")

        # Make empty list to store the max z value of each route
        maxz = []
        minz = []
        
        # Empty list to store the ticks of the z axis
        array_z = []

        # Iterate over all the lines and strip at the quotation marks. Only save split3: the route. 
        for i in range(len(lines) - 1):
            line = lines[i]
            splits = line.strip().split("\"")
            route = splits[3]  
            route = route.split(',')

            # Empty lists to store all the integers in the route and to store all the x y or z coordinates
            route_list = []
            x = []
            y = []
            z = []

            # Append the strings from the outputfile as integers to the route list
            for element in route:
                number = int(element.strip('( )[]'))
                route_list.append(number)

            # Append the x y and z coordinates from the routelist to the correct xyz list
            for i in range(0, len(route_list), 3):
                x.append(route_list[i])
                y.append(route_list[i+1])
                z.append(route_list[i+2])

            # Append the max z coordinate from each route
            maxz.append(max(z))
            minz.append(min(z))

            # Plot the route
            ax.plot(x,y,z)
       
        # Create correct ticks for the z axis
        for i in range(min(minz), max(maxz) + 1):
            array_z.append(i) 
        
        # Set correct z ticks
        ax.set_zticks(array_z)
        
        # Create tick spacing of 1 for the y and x axis
        tick_spacing = 1
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    # Create gates in the grid 
    gatesdict, _ = Grid.read_gates(1, gatesfilepath)
    keys = gatesdict.keys()
    for key in keys:
        x, y = gatesdict[key]
        ax.text(x, y, 0, key, color="black", fontweight="bold", bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
    
    # Set fontsize to 8
    ax.tick_params(axis='both', which='major', labelsize=8)
    
    # Show plot
    plt.show()



   