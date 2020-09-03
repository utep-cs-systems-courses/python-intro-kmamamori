"""
Name: Ken Amamori
CS Course: CS4375 - Operation System
Date: 2020 9/2
"""

import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

# receive an string(word) and an array(alphabetH) where each word is stored.
def putWord(word, alphabetH, wordsDict):
    if word in alphabetH[ord(word[0])-97]:  # check if
        wordsDict[word] = wordsDict[word] + 1  # increment the counting
    else:
        alphabetH[ord(word[0])-97].append(word)  # put on the register
        wordsDict[word] = 1  # counting started


# set input and output files
if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inFile = sys.argv[1]  # the first file on command
outFile = sys.argv[2]  # the third file on command

# first check to make sure program exists
if not os.path.exists("wordCount.py"):
    print("wordCount.py doesn't exist! Exiting")
    exit()

# array which keep track of word appearnce
alphabetH = [[], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], []]
wordsDict = {}  # keep track of

# Open text file with many words
with open(inFile, 'r') as i:  # prepare the car to read
    for line in i:  # iterate through each line
        line = line.strip()  # get rid of newline characters
        if len(line) != 0:
            # split the string into an array of string based on regex
            words = re.split(r'\s|-|\'|\"', line)
            for word in words:  # iterate the array of strings
                if word != '':
                    # checking the last character whether if is an alphabet
                    if ord(word[-1]) > 122 or ord(word[-1]) < 65:
                        word = word[:-1]  # remove the character
                    if word.isalpha():  # check if the word is an alphabet
                        word = word.lower()  # convert all upper case to lower case
                        # calling an function to build the array and couting
                        putWord(word, alphabetH, wordsDict)

# open the file to write the result
with open(outFile, 'w') as output:
    for alpha in alphabetH:  # iteral through
        alpha.sort()  # sort the array in order
        for word in alpha:  # iterate each word in the array
            output.write("%s %d\n" % (word, wordsDict[word]))
    output.close()
