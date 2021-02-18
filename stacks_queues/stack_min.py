# SOLVED? YES

# CTCI 3.2

# Design a stack which, in addition to push and pop, has a function min()
# that returns the minimum element.
# all methods should be O(1) time
class Stack:
    def __init__(self):
        self.top_index = -1
        self.values = []

    def peek(self):
        if self.isEmpty():
            raise EmptyStackError

        return self.values[self.top_index]

    def pop(self):
        if self.isEmpty():
            raise EmptyStackError

        popped = self.values[self.top_index]
        self.top_index -= 1
        return popped

    def push(self, val):
        self.top_index += 1
        self.values.append(val)

    def isEmpty(self) -> bool:
        return self.top_index == -1


class MinStack:
    def __init__(self):
        self.values = []
        self.size = 0
        self.minimum = Stack()

    def push(self, val):
        if self.isEmpty or self.minimum > val:
            self.minimum.push(val)

        self.values.append(val)
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise EmptyStackError

        self.size -= 1
        popped = self.values[self.size]

        if (popped == self.get_minimum()):
            self.minimum.pop()

        return popped

    def get_minimum(self):
        if self.isEmpty():
            raise EmptyStackError

        return self.minimum.peek()

    def isEmpty(self):
        return self.size == 0


class EmptyStackError(Exception):
    pass


min_stack = MinStack()
assert min_stack.isEmpty() == True
min_stack.push(1)
min_stack.push(-1)
assert min_stack.get_minimum() == -1
min_stack.push(-100)
assert min_stack.get_minimum() == -100
assert min_stack.isEmpty() == False
assert min_stack.pop() == -100
assert min_stack.get_minimum() == -1
min_stack.pop()
assert min_stack.get_minimum() == 1
