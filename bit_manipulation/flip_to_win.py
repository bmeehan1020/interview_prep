# SOLVED? NO

# CTCI 5.3
# Given integer, flip exactly one bit from 0 -> 1. Find length of longest sequence
# of 1s you could create

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
# def flip_bit_to_win(num):
#     if num == -1:
#         return float('inf')

#     bit_string = bin(num)[2:]
#     i = len(bit_string) - 1
#     max_chain = 1
#     length_before = 0
#     length_after = 0
#     while i:
#         if bit_string[i] == '1':
#             length_after += 1
#         else:
#             length_before = 0 if (i > 0 and
#                                   bit_string[i-1] == '0') else length_after
#             length_after = 0

#         max_chain = max([max_chain, length_before + length_after + 1])
#         i -= 1

#     return max_chain


# assert flip_bit_to_win(1775) == 8
# assert flip_bit_to_win(int('0b10110111', 2)) == 6
# assert flip_bit_to_win(0) == 1

# O(1) space instead of O(n)
# Best Conceivable Runtim is O(n) - must trav every bit
# avoid nested conditionals and nested while loops
