import operator


def escape(strings):
    string = ''
    lineCount = 0
    
    for x in strings:
        newLine = x.replace('\n', ' ')
        newLine = x.replace('\t', ' ')
        newLine.strip()
        if len(newLine):
            lineCount += 1
        string += newLine

    nonAlphaNumeric = ':;,/\\"\'_[]{}()|#*+-=<>~`°'

    for char in nonAlphaNmeric:
        string = string.replace(char, ' ')

    return [string, lineCount]

def wordStats(escapedString):
    words = {}
    sentences = {}
    wordCount = 0
    wordCountInSentence = 0
    sentenceCount = 0

    for word in escapedString.split(' '):
        wordCountInSentence +=1
        if "." in word or "!" in word or "?" in word:
            if wordCountInSentence != 0:
                if wordCountInSentence in sentences.keys():
                    sentences[wordCountInSentence] += 1
                else:
                    sentences[wordCountInSentence] = 1
                sentenceCount += 1
                wordCountInSentence = 0
            word = word.replace(".", "")
            word = word.replace("!", "")
            word = word.replace("?", "")
        wordCount += 1 
        if word != '':
            if word.lower() in words.keys():
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1

    sentences_final = sorted(sentences.items(), key=operator.itemgetter(0))

    words_final = sorted(words.items(), key=operator.itemgetter(1))
    words_final = words_final[::-1]

    return [words_final, wordCount, sentenceCount, sentences_final] 

def charStats(escapedString, order = 1):
    chars = {}
    charCount = 0

    for word in escapedString.split(' '):
        for char in word:
            if char != '':
                charCount += 1
                if char.lower() in chars.keys():
                    chars[char.lower()] += 1
                else:
                    chars[char.lower()] = 1

    # order by count
    if order == 1:
        char_final = sorted(chars.items(), key=operator.itemgetter(1))
        char_final = char_final[::-1]

    # order by alphabet
    if order == 2:
        char_final = sorted(chars.items(), key=operator.itemgetter(0))


    return [char_final, charCount]


def stats_basic(stat_file, lineCount, wordCount, charCount, sentenceCount):

    stat_file.write("Line count: " + str(lineCount) + "\n")
    stat_file.write("Word count: " + str(wordCount) + "\n")
    stat_file.write("Char count: " + str(charCount) + "\n")
    stat_file.write("Sentence count: " + str(sentenceCount) + "\n")
    stat_file.write("\n")
    stat_file.write("Words per line(avg): " + str(round(wordCount/lineCount, 2)) + "\n")
    stat_file.write("Words per sentence(avg): " + str(round(wordCount/sentenceCount, 2)) + "\n")
    stat_file.write("\n")
    stat_file.write("Char per line(avg): " + str(round(charCount/lineCount, 2)) + "\n")
    stat_file.write("Char per sentence(avg): " + str(round(charCount/sentenceCount, 2)) + "\n")
    stat_file.write("Char per word(avg): " + str(round(charCount/wordCount, 2)) + "\n")

def dunmpStats(stat_file, data):
    for item in data:
        stat_file.write(str(item[0]) + "," + str(item[1])  + "\n")
