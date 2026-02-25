import copy

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

# Copy lists
a = [1, 2, 3]
b = a

b.append(9)

print(a, b)

# shallow copy

c = a[:]
a.append(89)

shallow_copy = a.copy()
a.append(100)

print(c, shallow_copy)

# Deep copy
list_in_list = [[1, 2], 4]
list_copy = copy.deepcopy(list_in_list)
list_in_list[0][0] = 6
print(list_copy)

# id() -1 to 256

number_1 = 10
number_2 = 10
print(id(number_1), id(number_2))
print(hex(id(number_1)))

# bool
bool_variable = False

# == != > < >= <=
print(5 > 4.8)
print(True == 1)
print(False == 0)

# list comparison
first_list = [1, 2, 3]
second_list = [1, 2, 3]
copy_of_list = first_list[:]
print(first_list == second_list) # iterable comparison

print(first_list is second_list)
print(copy_of_list is first_list)

# in
print("Hello" in second_list)
print("Hello" not in second_list)

# logic operators
print(not(number_1 >= 10 or number_2 < 15))

# if else
age = 20
has_ticket = False

if age >= 18:
    if has_ticket:
        print("Entry allowed")
    else:
        print("Entry not allowed")
else:
    print("Enry not allowed, age is below 18")


result = "Adult" if age >= 18 else "Child"

print(result)

# match-case - in data book (switch case analogy)

# while for

numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    if numbers[index] == 3:
        index += 1
        continue

    if numbers[index] == 4:
        pass

    if numbers[index] == 5:
        print(numbers[index])
        break

    print(numbers[index])
    index += 1
else: #finally
    print("Else from while")

for item in numbers:
    print(item)

# range(start:stop:step) -> (0, 1, 2, 3, 4, 5)
my_range = range(5)
print(my_range) #range(0, 5)

for i in range(len(numbers)):
    print("I from range:", numbers[i])


for i in range(0, 10, 2):
    print("I from range:", i)