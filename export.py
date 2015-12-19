#!/usr/bin/env␣python¬
#␣-*-␣coding:␣utf-8␣-*-¬

import matplotlib.pyplot as plt
from matplotlib import rcParams


def showPlot(data, title, xlabel, ylabel):

    #rcParams['text.usetex'] = True
    #plt.rc('font', family='Arial')
    #plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
    plt.rc('font', family='DejaVu Sans')

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

