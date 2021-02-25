# SOLVED? YES!

# CTCI 4.2
# Given a sorted (increasing order) array with unique integer elements, write an
# algo to create a BST with minimal height
from bst import BSTNode


def minimal_tree(elements):
    if elements is None or len(elements) == 0:
        return None

    def minimal_tree_recur(elements, low, high):
        if low == high:
            return None
        index = (low + high) // 2
        node = BSTNode(elements[index])
        node.left = minimal_tree_recur(elements, low, index)
        node.right = minimal_tree_recur(elements, index + 1, high)
        return node

    return minimal_tree_recur(elements, 0, len(elements))


minimal_tree([1, 2, 5, 7, 9, 10])
assert minimal_tree(None) == None
assert minimal_tree([]) == None
single_elem = minimal_tree([1])
assert type(single_elem) == BSTNode
assert single_elem.val == 1
assert single_elem.left == None
assert single_elem.right == None

# other solutions have [0, len - 1], test if high < low,
# then recur on [low, mid -1] and [mid + 1, high]

# floor integer division: x // y
# 5 // 2 = 2
# 5 / 2 = 2.5
