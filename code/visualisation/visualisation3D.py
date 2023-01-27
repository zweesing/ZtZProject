import matplotlib.pyplot as plt


def visualize(outputfile):

    with open(outputfile) as outputfile:
        header = outputfile.readline()
        lines = outputfile.readlines()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

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

            ax.plot(x,y,z)


        plt.show()

if __name__ == "__main__":
    blip = visualize("output.csv")

   