carCount = int(input())
carOrder = [int(item) for item in input().split(" ")]
carOrder.reverse()
permutationPossible = True

deadEndStack = []
for required in range(1, carCount + 1):

    if len(deadEndStack) != 0 and deadEndStack[-1] == required:
        deadEndStack.pop()
        continue

    matchFound = False
    while len(carOrder) > 0:
        if carOrder[-1] == required:
            carOrder.pop()
            matchFound = True
            break
        deadEndStack.append(carOrder.pop())
    if matchFound:
        continue

    permutationPossible = False
    break

print("YES" if permutationPossible else "NO")
