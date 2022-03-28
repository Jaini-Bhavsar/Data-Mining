import time
start_time = time.time()

print("Choose and enter the number from menu:\n")
print("1.Amazon\n2.Best Buy\n3.K-mart\n4.Nike\n5.Custom Data")
n = int(input().strip())

if n == 1:
    # Amazon Dataset
    print("Amazon Dataset selected!")
    import pandas as pd

    df = pd.read_csv('amazon.csv')
    print(df)
    newTransaction = list([""] * len(df['Transaction']))
    dictTransactions = {}
    # perform run time encoding of transactions of in the for loop
    for i in range(0, len(df['Transaction'])):
        tempStr = ""
        for sstr in df['Transaction'][i].split(","):
            if sstr.strip() == 'A Beginner’sGuide':
                tempStr = tempStr + 'A'
                dictTransactions['A'] = 'A Beginner’sGuide'

            elif sstr.strip() == 'Java: The Complete Reference':
                tempStr = tempStr + 'B'
                dictTransactions['B'] = 'Java: The Complete Reference'

            elif sstr.strip() == 'JavaFor Dummies':
                tempStr = tempStr + 'C'
                dictTransactions['C'] = 'JavaFor Dummies'

            elif sstr.strip() == 'Android Programming: The Big Nerd Ranch':
                tempStr = tempStr + 'D'
                dictTransactions['D'] = 'Android Programming: The Big Nerd Ranch'

            elif sstr.strip() == 'Head First Java 2nd Edition':
                tempStr = tempStr + 'E'
                dictTransactions['E'] = 'Head First Java 2nd Edition'

            elif sstr.strip() == 'Beginning Programming with Java':
                tempStr = tempStr + 'F'
                dictTransactions['F'] = 'Beginning Programming with Java'

            elif sstr.strip() == 'Java 8 Pocket Guide':
                tempStr = tempStr + 'G'
                dictTransactions['G'] = 'Java 8 Pocket Guide'

            elif sstr.strip() == 'C++ Programming in Easy Steps':
                tempStr = tempStr + 'H'
                dictTransactions['H'] = 'C++ Programming in Easy Steps'

            elif sstr.strip() == 'Effective Java (2nd Edition)':
                tempStr = tempStr + 'I'
                dictTransactions['I'] = 'Effective Java (2nd Edition)'

            elif sstr.strip() == 'HTML and CSS: Design and Build Websites':
                tempStr = tempStr + 'J'
                dictTransactions['J'] = 'HTML and CSS: Design and Build Websites'

        newTransaction[i] += tempStr
    df["NewTransaction"] = newTransaction

elif n == 2:
    # Best Buy Dataset
    print("Best Buy Dataset selected!")
    import pandas as pd

    df = pd.read_csv('best_buy.csv')
    print(df)
    newTransaction = list([""] * len(df['Transaction']))
    dictTransactions = {}
    # perform run time encoding of transactions of in the for loop
    for i in range(0, len(df['Transaction'])):
        tempStr = ""
        for sstr in df['Transaction'][i].split(","):
            if sstr.strip() == 'Digital Camera':
                tempStr = tempStr + 'A'
                dictTransactions['A'] = 'Digital Camera'

            elif sstr.strip() == 'Lap Top':
                tempStr = tempStr + 'B'
                dictTransactions['B'] = 'Lap Top'

            elif sstr.strip() == 'Desk Top':
                tempStr = tempStr + 'C'
                dictTransactions['C'] = 'Desk Top'

            elif sstr.strip() == 'Printer':
                tempStr = tempStr + 'D'
                dictTransactions['D'] = 'Printer'

            elif sstr.strip() == 'Flash Drive':
                tempStr = tempStr + 'E'
                dictTransactions['E'] = 'Flash Drive'

            elif sstr.strip() == 'Microsoft Office':
                tempStr = tempStr + 'F'
                dictTransactions['F'] = 'Microsoft Office'

            elif sstr.strip() == 'Speakers':
                tempStr = tempStr + 'G'
                dictTransactions['G'] = 'Speakers'

            elif sstr.strip() == 'Lap Top Case':
                tempStr = tempStr + 'H'
                dictTransactions['H'] = 'Lap Top Case'

            elif sstr.strip() == 'Effective Java (2nd Edition)':
                tempStr = tempStr + 'I'
                dictTransactions['I'] = 'Effective Java (2nd Edition)'

            elif sstr.strip() == 'Anti-Virus':
                tempStr = tempStr + 'J'
                dictTransactions['J'] = 'Anti-Virus'

            elif sstr.strip() == 'External Hard-Drive':
                tempStr = tempStr + 'K'
                dictTransactions['K'] = 'External Hard-Drive'

        newTransaction[i] += tempStr
    df["NewTransaction"] = newTransaction

elif n == 3:
    # KMart Dataset
    print("KMart Dataset selected!")
    import pandas as pd

    df = pd.read_csv('kmart.csv')
    print(df)
    newTransaction = list([""] * len(df['Transaction']))
    dictTransactions = {}
    # perform run time encoding of transactions of in the for loop
    for i in range(0, len(df['Transaction'])):
        tempStr = ""
        for sstr in df['Transaction'][i].split(","):
            if sstr.strip() == 'Quilts':
                tempStr = tempStr + 'A'
                dictTransactions['A'] = 'Quilts'

            elif sstr.strip() == 'Bedspreads':
                tempStr = tempStr + 'B'
                dictTransactions['B'] = 'Bedspreads'

            elif sstr.strip() == 'Decorative Pillows':
                tempStr = tempStr + 'C'
                dictTransactions['C'] = 'Decorative Pillows'

            elif sstr.strip() == 'Bed Skirts':
                tempStr = tempStr + 'D'
                dictTransactions['D'] = 'Bed Skirts'

            elif sstr.strip() == 'Sheets':
                tempStr = tempStr + 'E'
                dictTransactions['E'] = 'Sheets'

            elif sstr.strip() == 'Shams':
                tempStr = tempStr + 'F'
                dictTransactions['F'] = 'Shams'

            elif sstr.strip() == 'Bedding Collections':
                tempStr = tempStr + 'G'
                dictTransactions['G'] = 'Bedding Collections'

            elif sstr.strip() == 'Kids Bedding':
                tempStr = tempStr + 'H'
                dictTransactions['H'] = 'Kids Bedding'

            elif sstr.strip() == 'Embroidered Bedspread':
                tempStr = tempStr + 'I'
                dictTransactions['I'] = 'Embroidered Bedspread'

            elif sstr.strip() == 'Towels':
                tempStr = tempStr + 'J'
                dictTransactions['J'] = 'Towels'

        newTransaction[i] += tempStr
    df["NewTransaction"] = newTransaction

elif n == 4:
    # Nike Dataset
    print("Nike Dataset selected!")
    import pandas as pd

    df = pd.read_csv('nike.csv')
    print(df)
    newTransaction = list([""] * len(df['Transaction']))
    dictTransactions = {}
    # perform run time encoding of transactions of in the for loop
    for i in range(0, len(df['Transaction'])):
        tempStr = ""
        for sstr in df['Transaction'][i].split(","):
            if sstr.strip() == 'Running Shoe':
                tempStr = tempStr + 'A'
                dictTransactions['A'] = 'Running Shoe'

            elif sstr.strip() == 'Soccer Shoe':
                tempStr = tempStr + 'B'
                dictTransactions['B'] = 'Soccer Shoe'

            elif sstr.strip() == 'Socks':
                tempStr = tempStr + 'C'
                dictTransactions['C'] = 'Socks'

            elif sstr.strip() == 'Swimming Shirt':
                tempStr = tempStr + 'D'
                dictTransactions['D'] = 'Swimming Shirt'

            elif sstr.strip() == 'Dry Fit V-Neck':
                tempStr = tempStr + 'E'
                dictTransactions['E'] = 'Dry Fit V-Neck'

            elif sstr.strip() == 'Rash Guard':
                tempStr = tempStr + 'F'
                dictTransactions['F'] = 'Rash Guard'

            elif sstr.strip() == 'Sweatshirts':
                tempStr = tempStr + 'G'
                dictTransactions['G'] = 'Sweatshirts'

            elif sstr.strip() == 'Hoodies':
                tempStr = tempStr + 'H'
                dictTransactions['H'] = 'Hoodies'

            elif sstr.strip() == 'Tech Pants':
                tempStr = tempStr + 'I'
                dictTransactions['I'] = 'Tech Pants'

            elif sstr.strip() == 'Modern Pants':
                tempStr = tempStr + 'J'
                dictTransactions['J'] = 'Modern Pants'

        newTransaction[i] += tempStr
    df["NewTransaction"] = newTransaction

elif n == 5:
    # Custom Dataset
    print("Custom Dataset selected!")
    import pandas as pd

    df = pd.read_csv('custom.csv')
    print(df)
    newTransaction = list([""] * len(df['Transaction']))
    dictTransactions = {}
    # perform run time encoding of transactions of in the for loop
    for i in range(0, len(df['Transaction'])):
        tempStr = ""
        for sstr in df['Transaction'][i].split(","):
            if sstr.strip() == 'ink':
                tempStr = tempStr + 'A'
                dictTransactions['A'] = 'ink'

            elif sstr.strip() == 'pen':
                tempStr = tempStr + 'B'
                dictTransactions['B'] = 'pen'

            elif sstr.strip() == 'cheese':
                tempStr = tempStr + 'C'
                dictTransactions['C'] = 'cheese'

            elif sstr.strip() == 'bag':
                tempStr = tempStr + 'D'
                dictTransactions['D'] = 'bag'

            elif sstr.strip() == 'juice':
                tempStr = tempStr + 'E'
                dictTransactions['E'] = 'juice'

            elif sstr.strip() == 'milk':
                tempStr = tempStr + 'F'
                dictTransactions['F'] = 'milk'

            elif sstr.strip() == 'eggs':
                tempStr = tempStr + 'G'
                dictTransactions['G'] = 'eggs'

            elif sstr.strip() == 'bread':
                tempStr = tempStr + 'H'
                dictTransactions['H'] = 'bread'

            elif sstr.strip() == 'napkins':
                tempStr = tempStr + 'I'
                dictTransactions['I'] = 'napkins'

            elif sstr.strip() == 'sugar':
                tempStr = tempStr + 'J'
                dictTransactions['J'] = 'sugar'

        newTransaction[i] += tempStr
    df["NewTransaction"] = newTransaction

print(dictTransactions)

print("Choose the option for minimum support format:\n1. Percentage\n2. Natural Number")
n = int(input().strip())
if n == 1:
    minSupPercentage = int(input().strip())
    minSup = (minSupPercentage * len(df['Transaction'])) // 100
elif n == 2:
    minSup = int(input())
print("Minimum Support Count : ", minSup)

print("Choose the option for minimum confidence format:\n1. Percentage\n2. Floating Number")
n = int(input().strip())
if n==1:
    minConfidencePercentage = int(input().strip())
    minConfidence = minConfidencePercentage / 100
elif n==2:
    minConfidence = float(input())
print("Minimum Confidence: ", minConfidence)

myList = list(df['NewTransaction'])
myList

#function for counting the frequency of items in candidate sets by scanning the transactions
def generate_Candidate(c, transactions):
    itemsInC = []
    for key in c.keys():
        itemsInC.append(key)
    for i in range(0, len(transactions)):
        tid = transactions[i]
        for j in range(0, len(itemsInC)):
            item = itemsInC[j]
            count = 0
            for k in range(0, len(item)):
                atkthpos = item[k] + ""
                if tid.find(atkthpos) >= 0:
                    count = count + 1
            if count == len(item):
                val = c[itemsInC[j]]
                val = val + 1
                c[item] = val
    return c

#function for generating k-item candidate sets by joining the (k-1)frequent itemsets
def join(l):
    c = {}
    itemInL = []
    for key in l.keys():
        itemInL.append(key)
    for i in range(0, len(itemInL)):
        for j in range(i+1, len(itemInL)):
            forchecki = itemInL[i][0:len(itemInL[i])-1]
            forcheckj = itemInL[j][0:len(itemInL[j])-1]
            if forchecki == forcheckj:
                newPotentialCandidate = itemInL[i] + itemInL[j][len(itemInL[j])-1]
                c[newPotentialCandidate] = 0
    return c

#function for generating frequent itemsets by checking the itemsets frequency with minimum support
def generate_frequent_set(transactions, minSup, c):
    l = {}
    nList = []
    for key in c.keys():
        nList.append(key)
    for i in range(0, len(nList)):
        support = c[nList[i]]
        if support >= minSup:
            l[nList[i]] = support
    return l

transactions = myList
finalDict = {}
DictForSubsetCounts = {}
print(transactions)
c = {}
for i in range(0, len(transactions)):
    tid = transactions[i]
    for j in range(0, len(tid)):
        ch = tid[j]
        if ch in c.keys():
            val = c[ch]
            val = val + 1
            c[ch] = val
        else:
            c[ch] = 1
print("C1 => ", c)
l = generate_frequent_set(transactions, minSup, c)
finalDict.update(l)
DictForSubsetCounts.update(l)
print("L1 => ", l)
counter = 2
while len(c) > 0:
    c = join(l)
    print("C", counter, " (by joining) L", (counter - 1), " => ", c)

    # c = prune(c, l)
    # print("C", counter, " (by pruning) => ", c)

    c = generate_Candidate(c, transactions);
    DictForSubsetCounts.update(c)
    print("C", counter, " (with support count) => ", c);

    l = generate_frequent_set(transactions, minSup, c)
    finalDict.update(l)
    DictForSubsetCounts.update(l)
    print("L", counter, " => ", l);

    counter = counter + 1

tmpDict = DictForSubsetCounts
keysInDictForSubsetCounts = list(DictForSubsetCounts.keys())
from itertools import permutations

for key in keysInDictForSubsetCounts:
    val = tmpDict.get(key)
    perm = [''.join(p) for p in permutations(key)]
    for p in perm:
        DictForSubsetCounts[p] = val
print("\nDictionary for rule generation =>\n")
print(DictForSubsetCounts)

dictKeys = finalDict.keys()
print(dictKeys)

print("Rules Generated are as follows:\n\n")
for individualString1 in dictKeys:
    for individualString2 in dictKeys:
        flag = 0
        for c in individualString1:
            if c in individualString2:
                flag = 1
                break
        if flag!=1:
            if (individualString1+individualString2) in DictForSubsetCounts.keys():
                confVal = int(DictForSubsetCounts.get(individualString1+individualString2))/DictForSubsetCounts.get(individualString1)
                if confVal >= minConfidence:
                    for char in individualString1:
                        print(char+" : "+dictTransactions[char])
                    for char in individualString2:
                        print(char+" : "+dictTransactions[char])
                    print(individualString1+' -> '+individualString2)
                    print("Confidence Value : " + str(confVal))
                    print()
                    print()
    print()
    print()

print("--- The Brute Force algorithm now executed takes: %s seconds ---" % (time.time() - start_time))