def generate_hist(sourceDict, filename = "output.txt"):
    length = len(sourceDict)
    items = sorted(sourceDict.items(), key=lambda tpl: tpl[0])
    quantities = [item[1] for item in items]

    height = max(quantities)
    result = [[] for i in range(height + 1)]

    for lineNo in range(height):
        for symbolNo in range(length):

            if quantities[symbolNo] >= height - lineNo:
                result[lineNo].append('#')
            else:
                result[lineNo].append(' ')

    result[height] = [item[0] for item in items]

    with open(filename, "w") as file:
        for line in result:
            print("".join(line), file=file)


with open("input.txt", "r") as file:
    inputString = file.read()

symbolCount = {symbol: 0 for symbol in set(inputString)}

for symbolRaw in inputString:
    symbolCount[symbolRaw] = symbolCount[symbolRaw] + 1

symbolCount.pop(' ', None)
symbolCount.pop('\n', None)

generate_hist(symbolCount)
