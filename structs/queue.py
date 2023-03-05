class Queue:
    _base: list[int]
    _size: int

    def __init__(self):
        self._base = []
        self._size = 0

    def push(self, elem : int):
        self._base.append(elem)
        self._size = self._size + 1
        print("ok")
        return True

    def pop(self):
        try:
            print(self._base.pop(0))
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

queue = Queue()

commands = {"push": lambda x: queue.push(int(x[1])),
            "pop": lambda x: queue.pop(),
            "front": lambda x: queue.front(),
            "size": lambda x: queue.size(),
            "clear": lambda x: queue.clear(),
            "exit": lambda x: False}

running = True

while running:
    args = input().split()
    running = commands[args[0]](args)
print("bye")
