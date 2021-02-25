# SOLVED? NO

# CTCI 4.1
# given directed graph and two nodes (S,E), design algo to find whether
# there is a route from S to E

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

from collections import deque
from enum import Enum, auto


class State(Enum):
    UNVISITED = auto()
    VISITING = auto()
    VISITED = auto()


def route_between_nodes(graph, start, end):
    if start == end:
        return True

    for node in graph.nodes:
        node.state = State.UNVISITED

    queue = deque()
    queue.append(start)

    while queue:
        found = queue.popleft()
        found.state = State.VISITING
        for node in found.adjacents:
            if node.state == State.UNVISITED:
                if node == end:
                    return True
                else:
                    queue.append(node)
        node.state = State.VISITED

    return False
    # check if start == end, short circuit True
    # during trav, if found end, return True
