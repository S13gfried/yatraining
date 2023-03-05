def children(index):
    return [index * 2 + 1, index * 2 + 2]


def parent(index):
    return (index - 1) // 2


class Heap:
    _body: list[int]
    _size: int

    def __init__(self, body = []):
        self._body = body
        self._size = len(body)

    def swap(self, index1, index2):
        self._body[index1], self._body[index2] = self._body[index2], self._body[index1]

    def push(self, obj):
        index = len(self._body)
        self._body.append(obj)
        self._size = self._size + 1

        while index != 0 and self._body[parent(index)] < obj:
            self.swap(index, parent(index))
            index = parent(index)

    def top(self):
        return self._body[0]

    def size(self):
        return self._size

    def pop(self):
        ans = self._body[0]
        new_top = self._body[-1]

        self._body[0] = new_top
        index = 0

        while children(index)[1] < len(self._body):
            child1 = self._body[children(index)[0]]
            child2 = self._body[children(index)[1]]

            if child1 > new_top and child1 >= child2:
                self.swap(index, children(index)[0])
                index = children(index)[0]
            elif child2 > new_top and child2 >= child1:
                self.swap(index, children(index)[1])
                index = children(index)[1]
            else:
                break

        self._size = self._size - 1
        self._body.pop()
        return ans


elementCount = int(input())
elements = [int(item) for item in input().split(" ")]

heap = Heap(elements)

ans = []
for index in range(elementCount):
    ans.insert(0, heap.pop())

print(" ".join([str(elem) for elem in ans]))
