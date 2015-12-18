import matplotlib.pyplot as plt


def showPlot(data):

    x = []
    xstick = []
    y = []

    x = list(range(len(data)))

    for i in data:
        a,b = i
        xstick.append(a)
        y.append(b)

    print(x)
    print(y)
    print( xstick)
    plt.xticks(x, xstick)
    plt.bar(x, y)

    plt.xlabel("a")
    plt.ylabel("b")
    plt.title("title")
    #plt.legend()
    plt.show()

