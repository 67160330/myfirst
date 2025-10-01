class Stack:
    def __init__(self, stack):
        self.stack = list(stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self

    def peek(self):
        return self.stack

    def is_empty(self):
        if not self.stack:
            return "True"
        else:
            return "False"

    def size(self):
        return len(self.stack)


s = Stack([1, 2, 3, 4, 5])
print("Size after push:")
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())
