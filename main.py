#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import *
import codecs
import sys

def main(fileName, isList = False):
    graph = False
    if "-g" in fileName:
        graph = True
        fileName.remove("-g")

    secondRes = None 
    secondFileName = None
    while isList and len(fileName) > 1:
        secondFileName = fileName.pop()
        secondRes = completeStats(secondFileName)  
    print(fileName)
    fileName = fileName[0]
    res = completeStats(fileName, graph)

    if secondRes != None:
        txtRes = ""
        for x in res:
            txtRes += compareStats(x, res[x], secondRes[x]) + "\n"

        compareFile = codecs.open(fileName + '-com.txt', 'w', 'utf-8')
        compareFile.write(txtRes)
        compareFile.close()

if __name__ == '__main__':
    if len(sys.argv) == 4:
        main([sys.argv[1],sys.argv[2],sys.argv[3]], True)
    elif len(sys.argv) == 3:
        main([sys.argv[1],sys.argv[2]], True)
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("input")
