# SOLVED? NO, but close

# CTCI 5.1
# two 32-bit numbers N and M and two bit positions i and j
# Write a method that inserts M into N such that M starts at
# j and ends at i. Assume [j, i] can fit all of M

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
# def insertion(N, M, i, j):
#     high_mask = -1 << (j + 1)
#     low_mask = (1 << i) - 1
#     mask = high_mask | low_mask
#     shifted_m = M << i
#     return (N & mask) | shifted_m


# N = '0b10000000000'
# M = '0b10011'
# assert insertion(int(N, 2), int(M, 2), 2, 6) == int('0b10001001100', 2)
