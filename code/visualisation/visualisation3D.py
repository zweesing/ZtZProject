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
            for element in route:
                number = int(element.strip('( )[]'))
                route_list.append(number)
         
            for i in range(0, len(route_list), 2):
                x.append(route_list[i])
                y.append(route_list[i+1])
        
            z = []
            for i in range(len(x)):
                z.append(0)

            ax.plot(x,y,z)


        plt.show()

if __name__ == "__main__":
    blip = visualize("output.csv")

   