"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""


def frequencies(items):
    #print("Enter a list of items separated by commas: ")
    #for item in input().split(","):
        #items.append(item)
    #print(frequencies(items))
    frequenciesDict = {}
    count=0
    for thing in items:
        for counting in items:
            if thing == counting:
                count += 1
            else:
                next
        frequenciesDict[thing] = count
        count = 0
    return frequenciesDict



#print(frequencies(items))


