# SOLVED? NO

# CTCI 1.3
# Replace all spaces in a string with '%20'
# assume string has enough space at end, you are provided true length of string
# in place
# true length "test test  " = 9, ignores extra trailing space
def urlify(string, length):
    return None


    # """replace spaces with %20 and removes trailing spaces"""
    # # convert to list because Python strings are immutable
    # char_list = list(string)
    # space_count = string.count(" ", 0, length)
    # string = ""
    # new_index = length + space_count * 2
    # for i in reversed(range(length)):
    #     if char_list[i] == " ":
    #         # Replace spaces
    #         char_list[new_index - 3: new_index] = "%20"
    #         new_index -= 3
    #     else:
    #         # Move characters
    #         char_list[new_index - 1] = char_list[i]
    #         new_index -= 1
    # # convert back to string
    # return string.join(char_list)
print(urlify("test with spaces    ", 16))
print(urlify("t t t t      ", 7))
print(urlify("", 0))
print(urlify("   ", 1))
# String manipulation? edit backwards
