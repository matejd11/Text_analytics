#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import codecs
from export import *


def createDict(listOfTuples):
    res = {}
    for item in listOfTuples:
        itemA, itemB = item
        res[itemA] = itemB

    return res

def compareStats(name, resA, resB):
    res = "difference in " + name + ":"
    resTmp = None

    if name == "basic":
        for i in range(len(resA)):
            diff = resB[i] - resA[i] 
            if i == 0:
                res += "\n\tin line count: "
            elif i == 1:
                res += "\n\tin word count: "
            elif i == 2:
                res += "\n\tin char count: "
            elif i == 3:
                res += "\n\tin centences count:"
            res += str(diff)

    if name == "word":
        A = createDict(resA[0])
        B = createDict(resB[0])
        resTmp = {}

        for i in A:
            if i in B.keys():
                if not i in resTmp.keys():
                    resTmp[i] = B[i] - A[i]
            else:
                resTmp[i] = -A[i]

            for i in B:
                if i in A.keys():
                    if not i in resTmp.keys():
                        resTmp[i] = B[i] - A[i]
                else:
                    resTmp[i] = B[i]

    if name == "sentance":
        A = createDict(resA[0])
        B = createDict(resB[0])
        resTmp = {}

        for i in A:
            if i in B.keys():
                if not i in resTmp.keys():
                    resTmp[i] = float("{0:.5f}".format(B[i] - A[i]))
            else:
                resTmp[i] =  float("{0:.5f}".format(-A[i]))

        for i in B:
            if i in A.keys():
                if not i in resTmp.keys():
                    resTmp[i] = float("{0:.5f}".format(B[i] - A[i]))
            else:
                resTmp[i] = float("{0:.5f}".format(B[i]))

    if name == "char":
        A = createDict(resA[0])
        B = createDict(resB[0])
        resTmp = {}

        for i in A:
            if i in B.keys():
                if not i in resTmp.keys():
                    resTmp[i] = float("{0:.5f}".format(B[i] - A[i]))
            else:
                resTmp[i] =  float("{0:.5f}".format(-A[i]))

        for i in B:
            if i in A.keys():
                if not i in resTmp.keys():
                    resTmp[i] = float("{0:.5f}".format(B[i] - A[i]))
            else:
                resTmp[i] = float("{0:.5f}".format(B[i]))

    if resTmp != None:
        final = sorted(resTmp.items(), key=operator.itemgetter(1))
        final = final[::-1]
        for i in final:
            res += "\n\t" + str(i[0]) + ": " + str(i[1])

    return res

def completeStats(fileName, graph = False):
    inputFile = codecs.open(fileName + '.txt', 'r', 'utf-8')
    resultFile = codecs.open(fileName + '-basic.txt', 'w', 'utf-8')
    sentenceFile = codecs.open(fileName + '-sentences.txt', 'w', 'utf-8')
    wordFile = codecs.open(fileName + '-word.txt', 'w', 'utf-8')
    charFile = codecs.open(fileName + '-char.txt', 'w', 'utf-8')
    charFile2 = codecs.open(fileName + '-char-2.txt', 'w', 'utf-8')

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
    dumpPartialStats(wordFile, words_final)

    # writting sentence stats to file
    dumpPartialStats(sentenceFile, sentences_final)

    # writting character stats to file
    dumpPartialStats(charFile, char_final)

    # writting character stats to file
    dumpPartialStats(charFile2, char_final_2)

    inputFile.close()
    resultFile.close()
    sentenceFile.close()
    wordFile.close()
    charFile.close()
    charFile2.close()

    if graph:
        showPlot(char_final, "Početnosť písmen v súbore: " + fileName + ".txt", "písmena", "početnosť v intervale <0; 1>")
        showPlot(words_final, "Početnosť slov v súbore: " + fileName + ".txt", "slová", "počet", 100)

    res = {
        "basic" : [lineCount, wordCount, charCount, sentenceCount],
        "word" : [words_final],
        "sentance" : [sentences_final],
        "char" : [char_final, char_final_2]
    }

    return res

def escape(strings):
    string = ''
    lineCount = 0

    for x in strings:
        newLine = x.replace('\n', ' ')
        newLine = newLine.replace('\t', ' ')
        newLine.strip()
        if len(newLine):
            lineCount += 1
        string += newLine

    nonAlphaNumeric = ':;,/\\"\'_[]{}()|#*+-=<>~`°'

    for char in nonAlphaNumeric:
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
                    if char != "."  and char != "!" and char != "?":
                        chars[char.lower()] = 1

    for i in chars:
        chars[i] = float("{0:.5f}".format(chars[i] / charCount))

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

def dumpPartialStats(stat_file, data):
    for item in data:
        stat_file.write(str(item[0]) + "," + str(item[1])  + "\n")
