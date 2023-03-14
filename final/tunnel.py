operations = int(input())

cars = []
goods = {}

for i in range(operations):
    order = input().split()

    if order[0] == "add":
        count = int(order[1])
        name = order[2]
        if count > 0:
            if len(cars) == 0 or cars[-1][1] != name:
                cars.append((count, name))
            else:
                prev = cars.pop()
                cars.append((prev[0] + count, name))

            if name in goods:
                goods[name] += count
            else:
                goods[name] = count

    elif order[0] == "delete":
        count = int(order[1])
        while count > 0:
            deleted = cars.pop()
            residue = (deleted[0] - count, deleted[1])
            goods[deleted[1]] -= min(count, deleted[0])

            count -= deleted[0]
            if count < 0:
                cars.append(residue)

    elif order[0] == "get":
        name = order[1]
        if name in goods:
            print(goods[name])
        else:
            print(0)
