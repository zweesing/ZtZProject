from code.visualisation.visualisation3D import visualize
import matplotlib.pyplot as plt
import numpy as np


def show_visualisation():
    chip = 1

    gatesfilepath = f"data/chip_{chip}/print_{chip}.csv"
    visualize("results/greedy_sorted_chip1_netlist5/output8.csv", gatesfilepath)


def make_data(data_paths):
    """takes list of costs file locations and returns nested list with costs

    Args:
        data_paths (list): file locations

    Returns:
        list: nested list with costs
    """
    costlists = []
    for file in data_paths:
        costlist = []
        with open(file) as f:
            header = f.readline()
            lines = f.readlines()

            for line in lines:
                line = line.split(",")
                costlist.append(line[0])

        costlists.append(costlist)
    return costlists


# hist for netlist 3, trying some things

net3list_shuff = [
    "results/cost_results/costs_breadth_shuffled/breadth_shuffled_chip0_netlist3_costs.csv",
    "results/cost_results/costs_breadthext_shuffled/breadthext_shuffled_chip0_netlist3_costs.csv",
    "results/cost_results/costs_greedy_shuffled/greedy_shuffled_chip0_netlist3_costs.csv",
]
net3list_sort = [
    "results/cost_results/costs_breadth_sorted/breadth_sorted_chip0_netlist3_costs.csv",
    "results/cost_results/costs_breadthext_sorted/breadthext_sorted_chip0_netlist3_costs.csv",
    "results/cost_results/costs_greedy_sorted/greedysortedchip0net3.csv",
]

net3list_greedy = [
    "results/cost_results/costs_greedy_shuffled/greedy_shuffled_chip0_netlist3_costs.csv",
    "results/cost_results/costs_greedy_sorted/greedysortedchip0net3.csv",
]

netlist_breadth = []

leg_shuff = [
    "breadth_sorted",
    "breadthext_sorted",
    "greedy_sorted",
]

leg_sort = [
    "breadth_shuffled",
    "breadthext_shuffled",
    "greedy_shuffled",
]

# shuff
costlists = make_data(net3list_shuff)


bins_list = [20, 25, 30, 35, 40, 45, 50, 55, 60]
ticks = np.arange(20, 300, 5)

print(ticks)
plt.hist(costlists)
plt.legend(leg_shuff)
plt.yscale("log")
# plt.xticks(ticks)

plt.show()
