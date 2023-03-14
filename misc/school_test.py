seats, variants, row, side = int(input()), int(input()), int(input()), int(input())

seat = (row - 1)*2 + side
options = []

if seat - variants > 0:
    options.append([seat - variants, 0])
if seat + variants <= seats:
    options.append([seat + variants, 0])

if len(options) == 0:
    print(-1)
else:
    for option in options:
        option[1] = -abs((option[0] - 1) // 2 + 1 - row)*2 + (1 if (option[0] - 1) // 2 + 1 >= row else 0)
    best_option = max(options, key=lambda x: x[1])[0]
    print((best_option - 1) // 2 + 1, 2 - best_option % 2)
