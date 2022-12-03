def sortDict(dictionary):
    sortedDict = {}
    sortedValues = sorted(dictionary.values())
    sortedValues.reverse()

    for sortedValue in sortedValues:
        for dictValue in dictionary:
            if dictionary[dictValue] == sortedValue:
                sortedDict[dictValue] = dictionary[dictValue]
                dictionary.pop(dictValue, dictionary[dictValue])
                break

    return sortedDict


names = list(input().split())

for i in range(len(names)):
    names[i] = names[i].lower()

namesAndValues = dict()

difNames = set(names)
difNames = list(difNames)

for i in difNames:
    namesAndValues[i] = names.count(i)

namesAndValues = sortDict(namesAndValues)

for i in range(len(difNames)):
    print(list(namesAndValues.keys())[i], str(int(list(namesAndValues.values())[i] / len(names) * 100)) + "%")
