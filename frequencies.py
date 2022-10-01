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
        str(thing)
        for counting in items:
            str(counting)
            if thing == counting:
                count += 1
            else:
                next
        frequenciesDict[str(thing)] = count
        count = 0
    return frequenciesDict



#print(frequencies(items))


