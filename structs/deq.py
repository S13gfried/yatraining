class Deq:
    _base: list[int]
    _size: int

    def __init__(self):
        self._base = []
        self._size = 0

    def push_back(self, elem: int):
        self._base.append(elem)
        self._size = self._size + 1
        print("ok")
        return True

    def push_front(self, elem: int):
        self._base.insert(0, elem)
        self._size = self._size + 1
        print("ok")
        return True

    def pop_front(self):
        try:
            print(self._base.pop(0))
            self._size = self._size - 1
        except IndexError:
            print("error")
        return True

    def pop_back(self):
        try:
            print(self._base.pop())
            self._size = self._size - 1
        except IndexError:
            print("error")
        return True

    def front(self):
        try:
            print(self._base[0])
        except IndexError:
            print("error")
        return True

    def back(self):
        try:
            print(self._base[-1])
        except IndexError:
            print("error")
        return True

    def size(self):
        print(self._size)
        return True

    def clear(self):
        self._base = []
        self._size = 0
        print("ok")
        return True

    def exit(self):
        return False


deq = Deq()

commands = {"push_front": lambda x: deq.push_front(int(x[1])),
            "push_back": lambda x: deq.push_back(int(x[1])),
            "pop_front": lambda x: deq.pop_front(),
            "pop_back": lambda x: deq.pop_back(),
            "front": lambda x: deq.front(),
            "back": lambda x: deq.back(),
            "size": lambda x: deq.size(),
            "clear": lambda x: deq.clear(),
            "exit": lambda x: False}

running = True

while running:
    args = input().split()
    running = commands[args[0]](args)
print("bye")
