import sys
import re         # regular expression tools

inFile = sys.argv[1]  # the first text file
outFile = sys.argv[2]


# # receives a string(word) and an array which the word will be stored to check the length of the array
# def checkArraySize(word, letterArray):
#     if len(letterArray) < len(word):
#         for i in range(len(word)-len(letterArray)):
#             letterArray.append([])


# receive an string(word) and an array(alphabetH) where each word is stored.
def putWord(word, alphabetH, wordsDict):
    # checkArraySize(word, alphabetH[ord(word[0])-97])
    if word in alphabetH[ord(word[0])-97]:
        wordsDict[word] = wordsDict[word] + 1
    else:
        alphabetH[ord(word[0])-97].append(word)
        wordsDict[word] = 1


# [[] for i in range
alphabetH = [[], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], []]
wordsDict = {}

# Open text file with many words
with open(inFile, 'r') as i:
    for line in i:
        line = line.strip()
        if len(line) != 0:
            # print(line)
            words = re.split(r'\s|-|\'', line)
            # print(words)
            for word in words:
                # if 3 == 3:
                if word != '':
		                if ord(word[-1]) > 122 or ord(word[-1]) < 65:
		                    word = word[:-1]
		                if word.isalpha():
		                    word = word.lower()
                		    # print(word)
		                    putWord(word, alphabetH, wordsDict)
    # print(alphabetH)
    # print(wordsDict)

# for alpha in alphabetH:
# 	print(alpha)


with open(outFile, 'w') as output:
    # output.write('b')
    for alpha in alphabetH:
        alpha.sort()
        for word in alpha:
            # for word in wordSize:
            output.write("%s %d\n" % (word, wordsDict[word]))
    output.close()


# print(i)
# # for line in inputFile:
#         # get rid of newline characters
#         line = line.strip()
#         # split line on whitespace and punctuation
#         word = re.split('[ \t]', line)
#         if len(word) != 2:
#             print ("Badly formatted line, exiting. Bad line:\n %s" % line)
#             exit()
#         master[word[0]] = int(word[1])
#         words += 1
