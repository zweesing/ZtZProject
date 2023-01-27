from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
from code.classes.grid import Grid


def visualize(routes, gatesfilepath):

    colours = [
        "green",
        "yellow",
        "red",
        "blue",
        "black",
        "orange",
        "purple",
        "pink",
    ]
    route_counter = 0

    gatesdict, _ = Grid.read_gates(1, gatesfilepath)

    fig, ax = plt.subplots()
    ax.invert_yaxis()
    ax.set_title("Chips and Circuits")

    for route in routes:
        codes = [Path.MOVETO] + [Path.LINETO] * (len(route) - 1)

        # make it 2d if 3d
        if len(route[0]) == 3:
            new_route = []
            for coord in route:
                x, y, z = coord
                new_route.append((x, y))

            route = new_route

        vertices = route

        path = Path(vertices, codes)

        pathpatch = PathPatch(
            path,
            facecolor="none",
            edgecolor=colours[route_counter],
            linewidth=5,
            alpha=0.5,
        )
        route_counter += 1

        ax.add_patch(pathpatch)

    keys = gatesdict.keys()
    for key in keys:
        x, y = gatesdict[key]
        ax.text(x, y, key, backgroundcolor="black", color="white", fontweight="bold")

    ax.autoscale_view()

    plt.grid()
    plt.show()
