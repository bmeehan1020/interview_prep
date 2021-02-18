# SOLVED?

# CTCI 3.a1

# Describe how you could use a single array to implement 3 stacks

# Two Arrays you could have starting with the top at each end of the array,
# growing inward.
# - you'd have to handle the case where the size exceeds capacity.
# - overwrite other stack?

# [top1 -->       top2 -->       top3 --> ]

# pop(), peek(), push(), isEmpty()

class TripleStack:
    def __init__(self, size):
        self.num_stacks = 3
        self.size = size
        self.values = []


# ts = TripleStack(100)
# assert ts.num_stacks == 3
# assert ts.size == 100
