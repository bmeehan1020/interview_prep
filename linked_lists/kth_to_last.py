# SOLVED? NO

# CTCI 2.2

# Implement algo to find kth to last element of singly linked list
# assumptions: list is at least k?
# Node n .val, .next
def return_kth_to_last(llist, k):
    prev = curr = llist

    for _ in range(k):
        curr = curr.next

    while curr:
        prev = prev.next
        curr = curr.next

    return prev


# no i, _ for unreffed loop var
# if testing None, just use var as condition [if var:]
