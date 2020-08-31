import sys
import re         # regular expression tools

inFile = sys.argv[1]  # the first text file
# outFile = sys.argv[2]


class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self, size):
        self.item = []
        self.num_items = 0
        for i in range(size):
            self.item.append([])


# # Build HashTable
# def ht(f, f2):
#     print("\nBuilding hush table.\n")
#     print("Hash Table stats:")
#     H = HashTableC(19)  # create Hash Table of length 17
#     print("Initail table size", len(H.item))
#     for line in f:  # read line by line, glove
#         data = line.split(' ')
#         if data[0].isalpha():
#             H = InsertC(H, data)  # insert data
#     print("Total elements: ", H.num_items)
#     print("Final table size: ", len(H.item))
#     print("Load factor: ", H.num_items/len(H.item))
#     print("Percentage of empty lists:", c/len(H.item)*100)
#     print("Standard deviation of the lengths of the lists:", d)
#     print(H.item[int(d)+1])
#     print("\nReading word file to determine similarities.\n")
#     for line2 in f2:  # read line by line, word_pair
#         data2 = line2.split(',')
#         e0 = FindC(H, data2[0])  # return array if string found
#         e1 = FindC(H, data2[1])  # return array if string found


# #HT: find k and return array if found
# def FindC(H,k):
#     # Returns bucket (b) and index (i)
#     # If k is not in table, i == -1
#     b = h(k,len(H.item)) #get index
#     for i in range(len(H.item[b])): #traverse the node
#         if H.item[b][i][0] == k: #found
#             return H.item[b][i][1] #return array
#     return -1


alphabetH = [[], [], [], [], [], [], [], [], [], [], [], [],
             [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# Open text file with many words
with open(inFile, 'r') as i:
    # with open(inputFname, 'r') as inputFile:
    # lines = i.readLines()
    for line in i:
        line = line.strip()
        if len(line) != 0:
            words = re.split('[ \t]', line)
            for word in words:
                # if 3 == 3:
                if ord(word[-1]) > 122 or ord(word[-1]) < 65:
                    word = word[:-1]
                word = word.lower()
                print(word)


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
