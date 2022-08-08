class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # .remove removes the first occurence of the value. It does not removes values based on index.
        return self.items.remove(self.items[len(self.items)-1])
        # return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



s=Stack()

# print(s.isEmpty())

s.push(1)
s.push("2")
s.push(True)

s.pop()

print(s.size())
