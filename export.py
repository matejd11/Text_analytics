import matplotlib.pyplot as plt


def showPlot(data, title, xlabel, ylabel):

    x = []
    xstick = []
    y = []

    x = list(range(len(data)))

    for i in data:
        a,b = i
        xstick.append(a)
        y.append(b)

    plt.xticks(x, xstick)
    plt.bar(x, y)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    #plt.legend()
    plt.show()

