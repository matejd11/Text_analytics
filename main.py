from stats import *
import codecs

def main(fileName = 'test'):
	inputFile = codecs.open(fileName + '.txt', 'r', 'utf-8')
	r = open(fileName + '-basic.txt', 'w')
	s = open(fileName + '-sentences.txt', 'w')
	w = open(fileName + '-word.txt', 'w')
	c = open(fileName + '-char.txt', 'w')
	inputString = inputFile.read()

	strings = inputString.splitlines(True)

	escapedString, lineCount = escape(strings)

	words_final, wordCount, sentenceCount, sentences_final = wordStats(escapedString)

	dunmpStats(w, words_final)
	
	dunmpStats(s, sentences_final)

	char_final, charCount = charStats(escapedString)

	dunmpStats(c, char_final)

	stats_basic(r, lineCount, wordCount, charCount, sentenceCount)

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
