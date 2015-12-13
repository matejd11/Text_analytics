from stats import *
import sys

def main(fileName):
    secondRes = None 
    secondFileName = None
    if isinstance(fileName, list):
        secondFileName = fileName.pop()
        secondRes = completeStats(secondFileName)  
        fileName = fileName[0]
    res = completeStats(fileName)

    if secondRes != None:
        print("comperring res")
        for x in res:
            print(compareStats(x, res[x], secondRes[x]))
    

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main([sys.argv[1],sys.argv[2]])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("input")
