from stack import Stack

# CTCI 3.3 Stack of plates, start new stack when prev stack exceeds some threshhold
# push() pop() should behave same as a normal stack


class SetOfStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stacks = Stack()

    def pop(self):
        if self.stacks.is_empty():
            raise EmptySetStackError
        top_stack = self.stacks.peek()
        popped = top_stack.pop()
        if top_stack.is_empty():
            self.stacks.pop()
        return popped

    def push(self, val):
        if self.stacks.is_empty() or len(self.stacks.peek()) == self.stack_size:
            self.stacks.push(Stack())
        top_stack = self.stacks.peek()
        top_stack.push(val)
        return None

    def peek(self):
        if self.stacks.is_empty():
            raise EmptySetStackError
        top_stack = self.stacks.peek()
        return top_stack.peek()


class EmptySetStackError(Exception):
    pass
