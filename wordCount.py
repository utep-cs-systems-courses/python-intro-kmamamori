import sys
import re         # regular expression tools

inFile = sys.argv[1]  # the first text file
# outFile = sys.argv[2]


# class HashTableC(object):
#     # Builds a hash table of size 'size'
#     # Item is a list of (initially empty) lists
#     # Constructor
#     def __init__(self, size):
#         self.item = []
#         self.num_items = 0
#         for i in range(size):
#             self.item.append([])


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


# receives a string(word) and an array which the word will be stored to check the length of the array
def checkArraySize(word, letterArray):
    if len(letterArray) < len(word):
        for i in range(len(word)-len(letterArray)):
            letterArray.append([])


# receive an string(word) and an array(alphabetH) where each word is stored.
def putWord(word, alphabetH):
    checkArraySize(word, alphabetH[ord(word[0])-97])
    alphabetH[ord(word[0])-97][len(word)-1].append(word)
    # alphabetH[ord(word[0])-97].append(word)
    # print(word)


# [[] for i in range]
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
                # print(word)
                putWord(word, alphabetH)
    print(alphabetH)

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

"""
ar = [
    [
        [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], []#5
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], []#10
    ], [
        [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], []#15
    ], [
        [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], [], [], []#20
    ], [
        [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], []
    ], [
        [], [], [], [], [], [], [], [], [], []#23
    ], [

		], [

		], [
			#26
		]
]
"""

"""
arr1 = [
    [
        ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a',
            'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
        ['as', 'an', 'at', 'at', 'an', 'as', 'at',
            'an', 'at', 'an', 'an', 'as', 'as'],
        ['and', 'and', 'and', 'all', 'are', 'are', 'are', 'and', 'are', 'any', 'and', 'and', 'and', 'and', 'and', 'all', 'are', 'are', 'are', 'and', 'and', 'and', 'and', 'all', 'and', 'and', 'and', 'and', 'and', 'all', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'any', 'all',
            'and', 'and', 'and', 'and', 'all', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'all', 'and', 'act', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'are', 'and', 'and', 'are', 'all', 'and', 'all', 'and', 'and', 'and', 'and', 'and', 'all', 'and', 'and', 'and'],
        ['acts', 'away', 'ages', 'arms', 'ages', 'acts'],
        ['among', 'among', 'among', 'alter', 'alter',
            'after', 'alone', 'among', 'armed', 'among'],
        ['assume', 'abuses', 'assent', 'assent', 'attend',
            'assent', 'amount', 'armies', 'assent', 'armies'],
        ['another', 'abolish', 'against', 'already',
            'against', 'amongst', 'america'],
        ['absolute', 'absolute', 'affected', 'absolute', 'altering',
            'answered', 'attempts', 'appealed', 'absolved'],
        ['arbitrary', 'abdicated', 'acquiesce', 'assembled',
            'appealing', 'authority', 'alliances'],
        ['abolishing', 'accustomed', 'abolishing',
            'abolishing', 'attentions', 'allegiance'],
        ['accordingly'],
        ['annihilation'],
        ['accommodation'],
        ['appropriations', 'administration']
    ], [
        [],
        ['be', 'by', 'be', 'by', 'be', 'be', 'be', 'by', 'by', 'by', 'by',
         'be', 'by', 'by', 'by', 'by', 'be', 'by', 'by', 'by', 'be', 'be'],
        ['but'],
        ['been', 'bear', 'been', 'been', 'been'],
        ['bands', 'burnt', 'begun', 'bring'],
        ['bodies', 'bodies', 'beyond', 'become'],
        ['becomes', 'becomes', 'british', 'british', 'between'],
        ['benefits', 'brethren', 'brethren'],
        ['barbarous'],
        ['boundaries']
    ], [
        [],
        [],
        [],
        [],
        ['cause', 'civil', 'cases', 'cases', 'crown'],
        ['course', 'causes', 'causes', 'candid',
            'called', 'commit', 'coasts', 'common'],
        ['created', 'creator', 'certain', 'consent', 'changed', 'consent',
            'cutting', 'consent', 'cruelty', 'captive', 'country'],
        ['colonies', 'combined', 'colonies', 'charters', 'complete', 'conjured',
            'congress', 'colonies', 'colonies', 'conclude', 'contract', 'commerce'],
        ['connected', 'civilized', 'character', 'connexion'],
        ['constrains', 'compliance', 'conditions', 'conditions', 'connexions'],
        ['convulsions', 'constrained'],
        ['constitution'],
        ['circumstances', 'circumstances', 'consanguinity'],
        ['correspondence']
    ], [
        [],
        ['do', 'do', 'do'],
        [],
        ['duty', 'deaf'],
        ['death'],
        ['decent', 'design', 'direct', 'define', 'divine'],
        ['declare', 'dictate', 'distant', 'dangers', 'disavow', 'declare'],
        ['dissolve', 'deriving', 'disposed', 'domestic'],
        ['despotism', 'districts', 'dissolved', 'dependent', 'depriving',
            'declaring', 'declaring', 'destroyed', 'denounces', 'dissolved'],
        ['depository', 'desolation'],
        ['destructive', 'destruction', 'declaration'],
        ['dissolutions']
    ], [
        [],
        [],
        ['eat'],
        ['ends', 'each'],
        ['earth', 'equal', 'equal', 'evils', 'every', 'every'],
        ['events', 'effect', 'extend'],
        ['entitle', 'endowed', 'evinces', 'elected', 'exposed',
         'erected', 'english', 'example', 'excited', 'enemies'],
        ['exercise'],
        ['encourage', 'enlarging', 'establish'],
        ['experience', 'emigration'],
        ['established', 'endeavoured', 'endeavoured'],
        ['establishing', 'establishing', 'executioners'],
        ['establishment']
    ], [[], [], ['for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'for', 'fit', 'for', 'for', 'for', 'for', 'for', 'for', 'for'], ['from', 'form', 'form', 'from', 'from', 'from', 'free', 'fall', 'free', 'from', 'free', 'from', 'free', 'full', 'firm'], ['forms', 'facts', 'forms'], ['future', 'former'], ['foreign', 'foreign', 'friends', 'friends'], ['firmness', 'fortunes'], ['forbidden', 'fatiguing', 'frontiers'], ['foundation', 'formidable', 'foreigners'], [], [], ['fundamentally'], [], ['fellow-citizens']], [[], [], ['god'], ['good', 'good'], [], ['guards', 'giving'], ['general'], ['governed'], ['governors'], ['government', 'government', 'government', 'government', 'government', 'government'], ['governments', 'governments', 'governments'], [], ['great-britain', 'great-britain']], [[], ['he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he', 'he'], ['has', 'has', 'his', 'has', 'his', 'his', 'has', 'has', 'has', 'his', 'has', 'his', 'has', 'has', 'has', 'his', 'has', 'his', 'has', 'has', 'has', 'has', 'his', 'has', 'his', 'has', 'has', 'has', 'has'], ['have', 'hold', 'hath', 'have', 'here', 'head', 'high', 'have', 'have', 'have', 'have', 'have', 'here', 'have', 'have', 'have', 'hold', 'hold', 'have'], ['human', 'hands'], ['having', 'houses', 'hither', 'hither', 'humble', 'honour'], ['history', 'history', 'harrass'], [], ['happiness'], [], [], [], [], [], [], ['happiness.--that']], [[], ['in', 'it', 'it', 'is', 'it', 'in', 'it', 'is', 'it', 'is', 'is', 'is', 'in', 'in', 'in', 'in', 'in', 'in', 'in', 'it', 'in', 'is', 'in', 'is', 'in', 'in', 'is', 'is', 'in', 'in', 'in', 'in', 'in', 'in', 'is'], ['its', 'its', 'its'], ['into', 'into'], ['impel'], ['indeed', 'indian', 'injury'], [], ['injuries', 'invasion', 'imposing', 'invested'], ['institute', 'immediate', 'invasions', 'incapable', 'interrupt'], ['instituted', 'invariably', 'importance', 'instrument', 'inevitably', 'intentions'], ['inestimable', 'independent', 'inhabitants', 'introducing', 'inhabitants', 'independent', 'independent', 'independent'], [], ['insurrections']], [[], [], [], ['just', 'jury'], ['judge'], ['judges'], ['justice', 'justice', 'justice'], [], ['judiciary'], [], [], ['jurisdiction', 'jurisdiction']], [[], [], [], ['king', 'kept'], ['known'], [], ['kindred']], [[], [], ['let'], ['laws', 'life', 'long', 'long', 'laws', 'laws', 'laws', 'long', 'laws', 'laws', 'laws', 'laws', 'laws', 'levy'], ['light', 'large', 'large', 'lands', 'large', 'lives', 'large', 'lives'], ['laying', 'likely'], ['liberty'], [], ['legislate'], [], ['legislature', 'legislative', 'legislative', 'legislation', 'legislature'], ['legislatures', 'legislatures']], [[], [], ['men', 'men', 'may', 'may'], ['most', 'more', 'most', 'mean', 'made', 'mock', 'many', 'most', 'most', 'most', 'must'], ['manly'], ['marked'], ['mankind', 'mankind', 'murders', 'mankind'], ['measures', 'military', 'mutually'], ['multitude', 'merciless'], ['migrations'], ['mercenaries', 'magnanimity']], [[], [], ['new', 'not', 'new', 'now', 'new', 'new', 'nor'], ['name'], [], ['nature', 'nation', 'native'], [], ["nature's"], ['necessary', 'necessity', 'necessary', 'neglected', 'necessity'], [], [], ['neighbouring'], [], ['naturalization']], [[], ['of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'or', 'on', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'on', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'on', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'on', 'of', 'of', 'on', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'on', 'of', 'or', 'on', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'of', 'on', 'of'], ['one', 'off', 'our', 'out', 'our', 'our', 'our', 'off', 'our', 'our', 'our', 'our', 'our', 'our', 'own', 'out', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our', 'our'], ['over', 'only', 'once', 'only', 'over'], ['other', 'ought', 'ought', 'other', 'other'], ['object', 'object', 'others', 'others', 'others'], ['offices', 'offices'], ['opinions', 'obtained', 'opposing', 'officers', 'offences'], ['operation'], ['organizing', 'obstructed'], ['obstructing', 'oppressions']], [[], [], [], ['pass', 'pass', 'pass'], ['prove', 'peace', 'power', 'parts', 'power', 'peace', 'power', 'peace'], ['people', 'powers', 'powers', 'people', 'powers', 'public', 'people', 'people', 'places', 'public', 'people', 'powers', 'people', 'powers', 'people', 'people', 'prince', 'people', 'people', 'pledge'], ['pursuit', 'provide', 'patient', 'present', 'purpose', 'prevent', 'purpose', 'payment', 'perfidy', 'publish'], ['prudence', 'pursuing', 'pressing', 'province'], ['political', 'pretended', 'pretended', 'plundered', 'petitions', 'political'], ['principles', 'population', 'protecting', 'punishment', 'protection', 'paralleled', 'petitioned', 'protection', 'providence']], [[], [], [], [], [], [], [], [], [], ['quartering']], [[], [], [], ['rule', 'rule', 'rest'], ['right', 'right', 'right', 'right', 'right', 'ruler', 'right', 'right'], ['rights', 'rights', 'reduce', 'rights', 'render', 'render'], ['respect', 'refused', 'refused', 'records', 'refused', 'raising', 'ravaged', 'redress'], ['requires', 'repeated', 'returned', 'refusing', 'refusing', 'repeated', 'repeated', 'reminded', 'reliance'], ['remaining', 'rectitude'], ['relinquish', 'repeatedly'], [], [], [], ['representation', 'representative'], ['representatives']], [[], ['so', 'so'], [], ['such', 'such', 'seem', 'same', 'such', 'such', 'such', 'sole', 'such', 'sent', 'seas', 'same', 'seas', 'seas'], ['shall', 'shewn', 'state', 'sexes', 'stage', 'state'], ['should', 'secure', 'safety', 'should', 'suffer', 'states', 'should', 'states', 'swarms', 'should', 'states', 'system', 'states', 'states', 'states', 'states', 'sacred'], ['station', 'systems', 'subject', 'savages', 'supreme', 'support'], ['separate', 'security', 'salaries', 'standing', 'superior', 'scarcely', 'solemnly'], ['submitted', 'suspended', 'suspended', 'substance'], ['separation', 'sufferable', 'sufferance', 'suspending', 'settlement', 'separation'], [], ['self-evident']], [[], ['to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to', 'to'], ['the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'too', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the', 'the'], ['them', 'them', 'that', 'they', 'them', 'that', 'that', 'they', 'that', 'that', 'them', 'that', 'that', 'than', 'they', 'them', 'them', 'this', 'till', 'them', 'them', 'them', 'time', 'time', 'that', 'them', 'they', 'this', 'time', 'thus', 'them', 'time', 'time', 'them', 'them', 'ties', 'they', 'them', 'that', 'that', 'they', 'that', 'them', 'that', 'they', 'this'], ['these', 'their', 'these', 'these', 'their', 'these', 'their', 'train', 'their', 'their', 'throw', 'their', 'these', 'their', 'these', 'their', 'those', 'their', 'their', 'these', 'their', 'their', 'their', 'their', 'times', 'their', 'trial', 'these', 'trade', 'taxes', 'trial', 'tried', 'these', 'towns', 'taken', 'their', 'their', 'their', 'these', 'terms', 'their', 'their', 'these', 'these', 'these'], ['truths', 'tenure', 'troops', 'taking', 'tyrant', 'things'], ['tyranny', 'tyranny', 'therein', 'tyranny', 'totally', 'totally'], ['together'], ['transient', 'therefore', 'therefore'], ['themselves', 'themselves', 'themselves'], [], ['transporting', 'transporting']], [[], ['us', 'us', 'us', 'us', 'us', 'us', 'us', 'us', 'us', 'us', 'us'], [], [], ['under', 'unfit'], ['unless', 'unless', 'united', 'united'], ['utterly', 'unusual'], ['unworthy'], [], [], ['unalienable', 'usurpations', 'usurpations', 'usurpations'], [], ['uncomfortable', 'unwarrantable'], ['unacknowledged'], ['undistinguished']], [[], [], [], [], ['voice'], [], [], ['valuable']], [[], ['we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we', 'we'], ['war', 'war', 'war'], ['when', 'with', 'with', 'will', 'when', 'when', 'with', 'with', 'will', 'with', 'with', 'with', 'with', 'with'], ['which', 'which', 'which', 'while', 'which', 'which', 'world', 'would', 'which', 'world', 'works', 'whose', 'whose', 'which', 'which', 'would', 'which', 'world', 'which'], ['within', 'waging', 'warned'], ['whereby', 'without', 'without', 'without', 'warfare', 'wanting'], ['whenever'], ['wholesome'], ['whatsoever']], [], [], []]
"""