#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stats import *
import argparse
import codecs
import sys

def main(fileName, fileName2, graph):
    res = completeStats(fileName, graph)

    if fileName2 != None:
        secondRes = completeStats(fileName2)  

        txtRes = ""
        for x in res:
            txtRes += compareStats(x, res[x], secondRes[x]) + "\n"

        compareFile = codecs.open(fileName + '-com.txt', 'w', 'utf-8')
        compareFile.write(txtRes)
        compareFile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text analytics - Matej Dujava 445560', conflict_handler='resolve')
    parser.add_argument('firstFile', action="store", default="input", help='file name of first file')
    parser.add_argument('-s', '--secondFile', action="store", default= None, help='file name of second file')
    parser.add_argument('--secondFile', action="store", default= None, help='file name of second file')
    parser.add_argument('-g', action="store_true", default=False, help='show graph of char distribution')

    results = parser.parse_args()

    main(results.firstFile, results.secondFile, results.g)
