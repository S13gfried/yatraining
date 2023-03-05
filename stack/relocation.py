cityCount = int(input())
cityPrices = [int(item) for item in input().split(" ")]
destinations =[-1 for i in range(cityCount)]

stack = []  # (price, index)
for cityIndex in range(cityCount):
    while len(stack) > 0 and stack[-1][0] > cityPrices[cityIndex]:
        popped = stack.pop()
        destinations[popped[1]] = cityIndex
    stack.append((cityPrices[cityIndex], cityIndex))

print(" ".join([str(destination) for destination in destinations]))
