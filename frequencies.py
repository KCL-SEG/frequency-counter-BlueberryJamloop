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
        stringthing = str(thing)
        for counting in items:
            stringcounting = str(counting)
            if stringthing == stringcounting:
                count += 1
            else:
                next
        frequenciesDict[stringthing] = count
        count = 0
    return frequenciesDict



#print(frequencies(items))


