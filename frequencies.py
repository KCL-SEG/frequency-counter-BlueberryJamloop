"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

items = []

def frequencies(items):
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

print("Enter a list of items separated by commas: ")
for item in input().split(","):
    items.append(item)

print(frequencies(items))

for x in range (0,len(items)):
    print(items)

