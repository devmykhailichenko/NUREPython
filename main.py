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

list_1 = [1, 4, 5, 6]
list_copy = list_1
list_1[0] = 10

print(list_1, list_copy)

# Context manager