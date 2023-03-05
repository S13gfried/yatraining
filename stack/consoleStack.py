class Stack:
    _body: list[int]
    _size: int

    def __init__(self):
        self._body = []
        self._size = 0

    def push(self, n):
        self._body.append(n)
        self._size = self._size + 1
        print("ok")
        return True

    def pop(self):
        try:
            # return self._body.pop()
            print(self._body.pop())
            self._size = self._size - 1
        except IndexError:
            print("error")
        return True

    def back(self):
        try:
            # return self._body[-1].copy()
            print(self._body[-1])
        except IndexError:
            print("error")
        return True

    def size(self):
        # return self._size
        print(self._size)
        return True

    def clear(self):
        self._body = []
        self._size = 0
        print("ok")
        return True


stack = Stack()

commands = {"push": lambda x: stack.push(int(x[1])),
            "pop": lambda x: stack.pop(),
            "back": lambda x: stack.back(),
            "size": lambda x: stack.size(),
            "clear": lambda x: stack.clear(),
            "exit": lambda x: False}

running = True

while running:
    args = input().split()
    running = commands[args[0]](args)
print("bye")
