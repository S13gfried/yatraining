length, jumprange = (int(item) for item in input().split(" "))
reach = [0 for i in range(jumprange)]
reach[-1] = 1

for i in range(length - 1):
    reach.append(sum(reach[i:i+jumprange]))

print(reach[-1])
