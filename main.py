from stats import *
import codecs
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
        txtRes = ""
        for x in res:
            txtRes += compareStats(x, res[x], secondRes[x]) + "\n"

        compareFile = codecs.open(fileName + '-com.txt', 'w', 'utf-8')
        compareFile.write(txtRes)
        compareFile.close()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main([sys.argv[1],sys.argv[2]])
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("input")
