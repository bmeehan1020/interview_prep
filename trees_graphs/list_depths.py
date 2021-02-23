# SOLVED? NO

# CTCI 4.3
# Given a binary tree, design an algo which creates a linked list of all the
# nodes at each depth. (e.g. tree with depth D with have D linked lists)

#
#
#
#
#
#
#
#
#
#
#
#
#
# from collections import deque


# def list_of_depths(root):
#     if root is None:
#         return None

#     depths = []
#     root.depth = 0
#     depths[root.depth].insert(root)

#     queue = deque()
#     queue.append(root)
#     while queue:
#         node = queue.popleft()
#         if node.left:
#             node.left.depth = node.depth + 1
#             queue.append(node.left)
#             depths[node.left.depth].insert(node.left)
#         if node.right:
#             node.right.depth = node.depth + 1
#             queue.append(node.right)
#             depths[node.right.depth].insert(node.right)

#     return depths

# DFS + recursive call with depth param

# Use BFS BUT instead of queue, use previous depth list as the queue
# to add all children of next level at once
