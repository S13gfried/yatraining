sequence = input()

stack = []
isValid = True

opening = ('(', '[', '{')
pairs = {'(': ')',
         '[': ']',
         '{': '}'}

for bracket in sequence:
    if bracket in opening:
        stack.append(bracket)
    else:
        try:
            if pairs[stack.pop()] != bracket:
                isValid = False
                break
        except IndexError:
            isValid = False
            break

if len(stack) > 0:
    isValid = False

print("yes" if isValid else "no")
