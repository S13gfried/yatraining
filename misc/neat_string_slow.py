swapsAvailable = int(input())
line = input()

totalLength = len(line)
characters = set(line)

maxLength = 0

for character in characters:
    for start in range(totalLength):
        length = 0
        swaps = swapsAvailable

        while start + length != totalLength:
            if line[start + length] != character:
                swaps = swaps - 1
                if swaps < 0:
                    break
            length = length + 1

        maxLength = max(length, maxLength)

print(maxLength)