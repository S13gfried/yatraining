operationStack = []

# def find_composition(n):
#     if n == 1:
#         return [0, [1]]
#
#     options = [find_composition(n - 1)]
#     if n % 2 == 0:
#         options.append(find_composition(n/2))
#     if n % 3 == 0:
#         options.append(find_composition(n/3))
#     optimum = min(options, key=lambda x: x[0])
#
#     optimum[0] = optimum[0] + 1
#     optimum[1].append(n)
#     return optimum
#
#
arg = int(input())
# solution = find_composition(arg)
#
print(solution[0])
print(" ".join([str(item) for item in solution[1]]))
