from collections import deque


class Graph():
    def __init__(self, node_list):
        self.nodes = node_list


class Node():
    def __init__(self, name):
        self.name = name
        self.adjacents = []
        self.visited = False
        self.distance = float('inf')
        self.parent = None


def breadth_first_search(graph, source):
    """
    O(V + E)
    """
    for node in graph.nodes:
        node.visited = False
        node.distance = float('inf')
        node.parent = None
    source.distance = 0
    queue = deque()
    queue.append(source)
    while queue:
        found = queue.popleft()
        for adj in found.adjacents:
            if not adj.visited:
                adj.visited = True
                adj.distance = found.distance + 1
                adj.parent = found
                queue.append(adj)
        found.visited = True


v = Node('v')
r = Node('r')
s = Node('s')
w = Node('w')
t = Node('t')
x = Node('x')
u = Node('u')
y = Node('y')

v.adjacents = [r]
r.adjacents = [v, s]
s.adjacents = [r, w]
w.adjacents = [s, t, x]
t.adjacents = [w, x, u]
x.adjacents = [w, t, u, y]
u.adjacents = [t, x, y]
y.adjacents = [u, x]

g = Graph([v, r, s, w, t, x, u, y])

breadth_first_search(g, s)
for node in g.nodes:
    print(f"node {node.name} distance {node.distance}")


def depth_first_search(graph):
    """
    O(V + E)
    """
    class Time():
        def __init__(self, time):
            self.time = time

    for node in graph.nodes:
        node.visited = False
        node.parent = None
    clock = Time(0)
    for node in graph.nodes:
        if not node.visited:
            dfs_visit(graph, node, clock)


def dfs_visit(g, found, clock):
    clock.time += 1
    found.discovered = clock.time
    found.visited = True
    for node in found.adjacents:
        if not node.visited:
            node.parent = found
            dfs_visit(g, node, clock)
    clock.time += 1
    found.finished = clock.time


depth_first_search(g)
for node in g.nodes:
    print(
        f"node {node.name} discovered {node.discovered} finished {node.finished}")


def topological_sort(graph):
    """
    O(V + E)
    linear ordering of vertices, given graph is acyclic
    DFS but when each node finished, add to front of a linked list
    """
