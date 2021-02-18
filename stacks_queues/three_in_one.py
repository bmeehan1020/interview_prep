# SOLVED?

# CTCI 3.a1

# Describe how you could use a single array to implement 3 stacks

# Two Arrays you could have starting with the top at each end of the array,
# growing inward.
# - you'd have to handle the case where the size exceeds capacity.
# - overwrite other stack?

# [top1 -->       top2 -->       top3 --> ]

# pop(), peek(), push(), isEmpty()
class Stack:
    def __init__(self):
        self.top_index = -1
        self.values = []

    def peek(self):
        if self.isEmpty():
            raise EmptyStackException

        return self.values[self.top_index]

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException

        popped = self.values[self.top_index]
        self.top_index -= 1
        return popped

    def push(self, val):
        self.top_index += 1
        self.values.append(val)

    def isEmpty(self) -> bool:
        return self.top_index == -1


class EmptyStackException(Exception):
    """ Stack is empty """
    pass


s = Stack()
print(s.isEmpty())
s.push(1)
s.push(2)
print(s.isEmpty())
s.push(3)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())


class TripleStack:
    def __init__(self, size):
        self.num_stacks = 3
        self.size = size
        self.values = []


# ts = TripleStack(100)
# assert ts.num_stacks == 3
# assert ts.size == 100
