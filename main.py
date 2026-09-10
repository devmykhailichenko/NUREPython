#Syntax
x = int(10)
_y = float(67.78)
x9y = 89j
is_admin = False
user_name_surname = 'Ihor'
number1, number2, number3 = 1, 2, 3

print(x, _y, x9y, user_name_surname, number1, number2, number3)

# numeric operations
print(
     6 / 4,
    7 * 5,
    7 ** 2,
    12 % 10
)

number4 = 67
number4 -= 2

print(number4)

print(--number4) #-(-65)

number4 += 1
print(number4)

#Strings
print("Hello", 'Hello', 'hell\'o')
print('Hello,\n Ihor')
print(r'C:\\Users\\Ihor\\Desktop\\')
print("""
Hello
            hello
    hello
""")
print(3 * 'hello' + ', Ihor')
hello = 'Hello'
print(hello[0], hello[1:3])

name = "Ihor"
email = "ihor@gmail.com"
print(f"Hello, new user {name}, your email - {email}")

#Id and numbers: -5 256
user1_age = 21
user2_age = 21
user2_age += 3
print(f"variable a has {id(user1_age)} id", f"variable b has {id(user2_age)} id")

print(hex(id(user1_age)))

#bool
is_admin = False
print(is_admin, isinstance(is_admin, int))

a = 12
b = 13
c = 56

print(a > b, a < c, a == c, b != a, a >= c, b <= a)
print(5 == 5.0)
print(5 > 4.5)
print(True == 1)
print('apple' != 'apple', 'banana' < 'apple')

print(a < 20 and a > 9)
print(a < 10 or a > 9)
print(not(a < 10))

#if ... else
age = 16

if age >= 18:
    print("You are adult!")
else:
    print("You are not adult!")

score = 74
if score >= 90:
    print("Grade A")
    print("Congratulations!")
    hello = 'asdf'
elif score >= 75:
    print("Grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Grade FX")

