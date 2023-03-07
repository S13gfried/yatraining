import math
total = int(input())

positions = [int(item) for item in input().split()]
positions.sort()

optimal = [math.inf, positions[1] - positions[0]]

for i in range(total - 2):
    optimal.append(min(optimal[-2] + positions[i+2] - positions[i+1], optimal[-1] + positions[i+2] - positions[i+1]))

print(optimal[-1])
