# SOlVED? YES, but better exists

# CTCI 1.2
# Given two strings, write a method to decide if one is
# a permutation of the other

# O(m+n)
def check_permutation(str1, str2):
    return None
#


#


#

print(check_permutation("wow", "oww"))
print(check_permutation("wow", "abcd"))
print(check_permutation("", "a"))


# Solutions
# brute = check if len match, then compare sorted strings char by char
# char array = add str1 freq, subtract str2 freq, false if any elem 0
# Pythonic = collections.Counter creates dict with {key: elem, val: freq}
# or create dict by hand that behaves like Counter
