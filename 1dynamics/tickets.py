import math

customers = int(input())

deltaTimes = [[math.inf, math.inf, math.inf] for i in range(3)]
for i in range(3, customers + 3):
    deltaTimes.append([int(item) for item in input().split()])


optimal = [0, 0, 0]
for i in range(customers):
    options = []
    for purchaseSize in range(3):
        options.append(optimal[-purchaseSize-1] + deltaTimes[3-purchaseSize + i][purchaseSize])
    optimal.append(min(options))

print(optimal[-1])
