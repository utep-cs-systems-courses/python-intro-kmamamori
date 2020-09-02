import sys        # command line arguments
import re         # regular expression tools

inFile = sys.argv[1]  # the first file on command
outFile = sys.argv[2] # the third file on command

# receive an string(word) and an array(alphabetH) where each word is stored.
def putWord(word, alphabetH, wordsDict):
    if word in alphabetH[ord(word[0])-97]:
        wordsDict[word] = wordsDict[word] + 1
    else:
        alphabetH[ord(word[0])-97].append(word)
        wordsDict[word] = 1


alphabetH = [[], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], []]
wordsDict = {}

# Open text file with many words
with open(inFile, 'r') as i:
    for line in i:
        line = line.strip()
        if len(line) != 0:
            words = re.split(r'\s|-|\'', line)
            for word in words:
                if word != '':
		                if ord(word[-1]) > 122 or ord(word[-1]) < 65:
		                    word = word[:-1]
		                if word.isalpha():
		                    word = word.lower()
		                    putWord(word, alphabetH, wordsDict)

with open(outFile, 'w') as output:
    for alpha in alphabetH:
        alpha.sort()
        for word in alpha:
            # for word in wordSize:
            output.write("%s %d\n" % (word, wordsDict[word]))
    output.close()