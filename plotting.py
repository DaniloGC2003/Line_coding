import matplotlib.pyplot as plt

def binaryString_to_binaryList(binaryString):#recebe string binaria, retorna lista com bits
    bin_list = []
    for i in range(0, len(binaryString)):
        if binaryString[i] == '0':
            bin_list.append(0)
        else:
            bin_list.append(1)
    return bin_list

def plot_graph(voltage_list, y_axis):
    x_axis = []
    for i in range(0, len(voltage_list)):
        x_axis += 2 * [i]

    #plot.plot(x_axis, y_axis)
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis)
    #plt.show()

    return fig


