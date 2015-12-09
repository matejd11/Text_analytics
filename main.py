from stats import *
import codecs
import sys

def main(fileName = 'test'):
    inputFile = codecs.open(fileName + '.txt', 'r', 'utf-8')
    resultFile = open(fileName + '-basic.txt', 'w')
    sentenceFile = open(fileName + '-sentences.txt', 'w')
    wordFile = open(fileName + '-word.txt', 'w')
    charFile = open(fileName + '-char.txt', 'w')
    charFile2 = open(fileName + '-char-2.txt', 'w')

    # text from file. 
    inputString = inputFile.read()

    # list of lines
    strings = inputString.splitlines(True)

    # string witout non Alfanum characters (with . ! ?)
    escapedString, lineCount = escape(strings)

    # word and sentence statistics
    words_final, wordCount, sentenceCount, sentences_final = wordStats(escapedString)

    # char statistics orderd by count
    char_final, charCount = charStats(escapedString, 1)

    # char statistics orderd by Alphabet
    char_final_2, charCount_2 = charStats(escapedString, 2)

    # writting basic stats to file
    stats_basic(resultFile, lineCount, wordCount, charCount, sentenceCount)

    # writting word stats to file
    dunmpStats(wordFile, words_final)
    
    # writting sentence stats to file
    dunmpStats(sentenceFile, sentences_final)

    # writting character stats to file
    dunmpStats(charFile, char_final)

    # writting character stats to file
    dunmpStats(charFile2, char_final_2)

    inputFile.close()
    resultFile.close()
    sentenceFile.close()
    wordFile.close()
    charFile.close()
    charFile2.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
