word = input()
count = {letter: 0 for letter in set(word)}

for position in range(len(word)):
    count[word[position]] += (1 + position)*(len(word) - position)

for item in sorted(count.items(), key=lambda x: x[0]):
    print(item[0], ": ", item[1], sep="")
