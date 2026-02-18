# This is first comment

number1, number2, number3 = 1, 4, 5

print(number1, number2, number3)

# Numeric type operations

print(4 + 5, 6 - 9, 8 * 9, 6 / 2, 7 // 3, 4 % 3, 2 ** 4)

x = 45
x += 1

print(++x)

# Text type (str)
text_variable = 'First \n text!'

print(text_variable)

# Raw str
print('C:\some\name')
print(r'C:\some\name')

print(""" first text
      second text   
    third text
""")

my_own_str = "Hello" * 3
print(my_own_str + " world")
print("Hello" " first program")


# Str Indexing
my_python_str = "Python"

print(my_python_str, my_python_str[1])
print(my_python_str[-5])

print(len(my_python_str))

# f-string (formatted string literal)
name = "Alice"
age = 60

print(f"Hello {name}, you are {age} years old")

# List
my_first_list = [6, 7, 8, 9, 8.0, "Hello", True, 34 + 7j]
print(my_first_list, my_first_list[-6], my_first_list + [5, 6, 8])

my_first_list[1] = "ALEX"
my_first_list.append(89)

print(my_first_list)

# Slice list[start:stop:step]
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers[1:4])

print(numbers[:4])

print(numbers[4:])

numbers_copy = numbers[:]

print(numbers_copy)

print(numbers[:])

print(numbers[-3:])

print(numbers[::-1])

# Slice assignment
numbers[1:3] = [200, 100]
print(numbers)

numbers[1:3] = []
print(numbers)

numbers[:] = []
print(numbers)




