import math
import copy

days = int(input())
prices = tuple(int(input()) for index in range(days))
threshold = 100

matrix = [[[math.inf, []] for i in range(days + 1)] for j in range(days + 3)]
matrix[1][0][0] = 0

for day in range(days):
    for coupons in range(days + 1):
        options = [copy.deepcopy(matrix[coupons+1][day]), copy.deepcopy(matrix[coupons + 2][day])]
        options[0][0] += prices[day]
        options[1][1].append(day + 1)

        if prices[day] > threshold:
            options.append(copy.deepcopy(matrix[coupons][day]))
            options[-1][0] += prices[day]

        matrix[coupons + 1][day + 1] = min(options, key=lambda x: x[0])

best_index, best_sum = 0, math.inf
for index in range(days + 1):
    if best_sum >= matrix[index + 1][-1][0]:
        best_index, best_sum = index, matrix[index + 1][-1][0]

print(best_sum)
print(str(best_index) + " " + str(len(matrix[best_index + 1][-1][1])))
for day in matrix[best_index + 1][-1][1]:
    print(day)
