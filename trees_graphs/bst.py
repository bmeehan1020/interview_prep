from collections import deque


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def generate_binary_tree(node_list):
    """
    Return root of tree with values of input list
    reverse behavior of BFS

    e.g. [1,2,4,6, None, 7] =>
            1
        2       4
     6    X   7
    """
    if not node_list or len(node_list) == 0:
        return None
    input_queue = deque(node_list)
    root = BSTNode(input_queue.popleft())
    node_queue = deque()
    node_queue.append(root)

    while node_queue:
        # take out parent,
        # check input queue, make 1st into node, remove from input queue
        # make parent's left child
        # add to node queue
        # check input, make 1st into node, remove from input queue
        # make parent's right child
        # add to node queue

        parent = node_queue.popleft()
        if input_queue:
            if input_queue[0]:
                left = BSTNode(input_queue.popleft())
                node_queue.append(left)
                parent.left = left
            else:
                input_queue.popleft()
        if input_queue:
            if input_queue[0]:
                right = BSTNode(input_queue.popleft())
                node_queue.append(right)
                parent.right = right
            else:
                input_queue.popleft()

    return root


def isBinarySearchTree(root):
    if not root or not (root.left and root.right):
        return True

    return isBSTRecur(root, None, None)


def isBSTRecur(node, low, high):
    if not node:
        return True
    elif (low and node.val < low) or (high and node.val > high):
        return False
    else:
        return isBSTRecur(node.left, low, node.val) and isBSTRecur(node.right, node.val, high)


def pre_order_print(node):
    if node:
        print(node.val)
        pre_order_print(node.left)
        pre_order_print(node.right)


def in_order_print(node):
    if node:
        in_order_print(node.left)
        print(node.val)
        in_order_print(node.right)


def post_order_print(node):
    if node:
        post_order_print(node.left)
        post_order_print(node.right)
        print(node.val)
