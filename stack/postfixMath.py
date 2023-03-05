expression = input().split(" ")

stack = []
operators = ("+", "-", "*")
opDefinitions = {"+": lambda x, y: x + y,
                 "-": lambda x, y: y - x,
                 "*": lambda x, y: x * y}

for item in expression:
    if item in operators:
        result = opDefinitions[item](stack.pop(), stack.pop())
        stack.append(result)
    else:
        stack.append(int(item))

print(stack.pop())
