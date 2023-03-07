import copy
solutions = [[0, [1]]]

arg = int(input())

for i in range(1, arg):
    number = i + 1

    options = [solutions[i-1]]
    if number % 2 == 0:
        options.append(solutions[number // 2 - 1])
    if number % 3 == 0:
        options.append(solutions[number // 3 - 1])
    minimum = copy.deepcopy(min(options, key=lambda x: x[0]))

    minimum[0] = minimum[0] + 1
    minimum[1].append(number)
    solutions.append(minimum)

print(solutions[-1][0])
print(" ".join([str(item) for item in solutions[-1][1]]))
