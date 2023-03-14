# class SparseArray:
#     array = []
#
#     def __init__(self, new_array):
#         for new_elem in new_array:
#
#     def __getitem__(self, item):
#         return self.array[item]
#
#     def __setitem__(self, key, value):
#         self.array[key] = value

# def binary_search_int(target, metric, start = 0, end = 0, default = "left"):
#     go_right_if_equal = {"right" : True, "left" : False}
#     scope = [start, end]
#     while scope[0] != scope[1]:
#         if abs(metric(target) - metric(scope[0])) > abs(metric(target) - metric(scope[1])) or \
#           (abs(metric(target) - metric(scope[0])) == abs(metric(target) - metric(scope[1])) and go_right_if_equal[default]):
#             scope[0] = scope[1] - (scope[1] - scope[0]) // 2
#         else:
#             scope[1] = scope[0] + (scope[1] - scope[0]) // 2
#     return scope[0]


sticker_count = int(input())
sticker_input = [int(item) for item in input().split()]
# stickers = {}
stickers = []

for i in range(sticker_count):
    if sticker_input[i] not in stickers:
        stickers.append(sticker_input[i])
    #     stickers[number] += 1
    # else:
    #     stickers[number] = 1

# stickers_ordered = sorted([list(item) for item in stickers.items()], key=lambda x: x[0])
stickers.sort()

queries = int(input())
limits = [int(item) for item in input().split()]
for i in range(queries):
    total = 0
    limit = limits[i]
    for sticker in stickers:
        if sticker >= limit:
            break
        total += 1
        # else:
        #     if stickers_ordered[index][1] > 0:
        #         total += 1
        #         stickers_ordered[index][1] -= 1
    print(total)
