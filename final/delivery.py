orders = int(input)
time = []
for i in range(orders):
    time.append(tuple(int(item) for item in input().split()))

best = [[0, 0] for i in range(orders + 1)]
for i in range(orders):
