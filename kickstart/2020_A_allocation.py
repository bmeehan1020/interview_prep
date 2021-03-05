# SOLVED? YES!

t = int(input())
for i in range(1, t + 1):
    n, b = [int(d) for d in input().split(' ')]
    houses = [int(h) for h in input().split(' ')]
    houses = sorted(houses)
    num_houses = 0
    while b > 0 and n > 0:
        if (b - houses[len(houses) - n] < 0):
            break
        b -= houses[len(houses) - n]
        n -= 1
        num_houses += 1
    print(f"case #{i}: {num_houses}")

# Counting Sort - O(n+k) time/space
# where k is range of inputs
# not comparisons, but use elems as keys
