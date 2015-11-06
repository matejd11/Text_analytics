from stats import *
import codecs

def main():
	inputFile = codecs.open('text.txt', 'r', 'utf-8')
	r = open('result-basic.txt', 'w')
	s = open('result-sentences.txt', 'w')
	w = open('result-word.txt', 'w')
	c = open('result-char.txt', 'w')
	inputString = inputFile.read()

	strings = inputString.splitlines(True)

	escapedString, lineCount = escape(strings)

	words_final, wordCount, sentenceCount, sentences_final = wordStats(escapedString)

	stats(w, words_final)
	
	stats(s, sentences_final)

	char_final, charCount = charStats(escapedString)

	stats(c, char_final)

	stats_basic(r, lineCount, wordCount, charCount, sentenceCount)

	inputFile.close()
	r.close()
	w.close()
	s.close()
	c.close()

if __name__ == '__main__':
	main()
