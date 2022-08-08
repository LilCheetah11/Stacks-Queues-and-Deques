class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # In this case we're considering end of the deque as front
    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        # Remove and return item at index (default last)
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d=Deque()

# print(d.isEmpty())

# print(d.size())

d.addFront("Hello")
d.addRear("world")


# print(d.size())

# print(d.removeRear())

print(d.removeFront() + " " + d.removeRear())

print(d.size())
