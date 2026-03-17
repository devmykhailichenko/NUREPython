# file object -> cursor position, mode, buffer, functions
# Hello
# ^
# Hello
#   ^

# file = open("test.txt", "r")
#
# content = file.read()
#
# print(content)
#
# file.close()

file_cursor = open("test.txt", "r")

content = file_cursor.read(5)
print(content)

next_content = file_cursor.read(5)
print(next_content)

file_cursor.close()

# Context manager