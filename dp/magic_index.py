# SOLVED? NO

# CTCI 8.3
# A magic index in an array A[0...n-1] is defined to be an index such that
# A[i] = i. Given sorted array of distinct integers, write a method to find
# a magic index, if one exists, in array A
from typing import List


def magic_index(a: List[int]) -> int:
    if a is None or len(a) == 0:
        return None
    elif a[0] > (len(a) - 1) or a[len(a) - 1] < 0:
        return None

    i = 0
    j = len(a) - 1
    while(i < j):
        mid = (i + j) // 2
        if a[mid] == mid:
            return mid
        elif a[mid] < mid:
            i = mid + 1
        else:
            j = mid
    return None


a = [-5, -3, -1, 0, 2, 4, 5, 10, 12]
assert magic_index(a) == None
b = [-5, -3, -1, 0, 2, 4, 6, 10, 12]
assert magic_index(b) == 6
assert magic_index([]) == None
assert magic_index(None) == None
