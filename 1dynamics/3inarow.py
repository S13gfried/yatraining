previous = [1, 2, 4]

# the sequence can have three mutually exclusive endings: 0, 01 and 011. To achieve desired size, all of them can be
# appended to already calculated sequences of lesser lengths, specifically 1, 2 and 3 characters shorter,
# the sizes of which are stored in the "previous" array.

seqLength = int(input())
if seqLength < 3:
    print(previous[seqLength])
else:
    for iteration in range(seqLength - 2):
        previous.append(sum(previous))
        previous.pop(0)
    print(previous[-1])
