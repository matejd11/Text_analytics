from stats import *
import codecs
import sys

def main(fileName = 'test'):
	inputFile = codecs.open(fileName + '.txt', 'r', 'utf-8')
	r = open(fileName + '-basic.txt', 'w')
	s = open(fileName + '-sentences.txt', 'w')
	w = open(fileName + '-word.txt', 'w')
	c = open(fileName + '-char.txt', 'w')

	# text from file. 
	inputString = inputFile.read()

	# list of lines
	strings = inputString.splitlines(True)

	# string witout non Alfanum characters (with . ! ?)
	escapedString, lineCount = escape(strings)

	# word and sentence statistics
	words_final, wordCount, sentenceCount, sentences_final = wordStats(escapedString)

	# char statistics
	char_final, charCount = charStats(escapedString)

	# writting basic stats to file
	stats_basic(r, lineCount, wordCount, charCount, sentenceCount)

	# writting word stats to file
	dunmpStats(w, words_final)
	
	# writting sentence stats to file
	dunmpStats(s, sentences_final)

	# writting character stats to file
	dunmpStats(c, char_final)

	inputFile.close()
	r.close()
	w.close()
	s.close()
	c.close()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
