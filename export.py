import matplotlib.pyplot as plt


def showPlot(data):

    x = []
    y = []

    for i in data:
        x.append(data[i])
        y.append(i)

    plt.bar(x, y)

    plt.xlabel("a")
    plt.ylabel("b")
    plt.title("title")
    #plt.legend()
    plt.show()

showPlot({1:4,2:5})
