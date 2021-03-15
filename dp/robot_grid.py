# SOLVED? NO

from typing import List, Tuple, Set


class Point():
    def __init__(self, r, c, parent):
        self.row = r
        self.column = c
        self.parent = parent


def robot_path(r: int, c: int, blocked: List[Tuple[int, int]]) -> Point:
    failed = set()
    path = []
    if get_path(r-1, c-1, blocked, path, failed):
        return path
    return None


def get_path(r: int,
             c: int,
             blocked: List[Tuple[int, int]],
             path: List[Point],
             failed: Set[Point]) -> bool:

    if r < 0 or c < 0 or (r, c) in blocked:
        return False

    p = Point(r, c, None)

    if p in failed:
        return False

    isAtOrigin = r == 0 and c == 0
    if isAtOrigin or get_path(r, c-1, blocked, path, failed) or get_path(r-1, c, blocked, path, failed):
        path.append(p)
        return True

    failed.add(p)
    return False


path = robot_path(3, 4, set([(0, 1), (2, 2)]))
for p in path:
    print(f"({p.row}, {p.column})")
