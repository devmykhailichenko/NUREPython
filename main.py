# Functions
# __code__
# __globals__
# __defaults__
# __name__
# __annotations__
# __closure__
print(__name__)
# L - local, E - Enclosing, G - global, B - Built-in

def say_hello(name, surname, age=20):
    print(f"Hello user {name} {surname}. You are {age} ears old!")

say_hello("Ihor", "Mykh")

def sum_numbers(number_1, number_2) -> int:
    result = number_1 + number_2
    return result

numbers_result = sum_numbers(3, 4)

print(f"Result {numbers_result}")

print(sum_numbers(7, 8))
print(say_hello("sdfs", "sdfs", 89))


say_hello(surname="Mykhailichenko", age=28, name="Ihor")


def number_sum(*numbers_my_full):
    print(numbers_my_full, sum(numbers_my_full))

number_sum(1, 3, 4, 5, 6, 78, 8, 9, 9, 0)
number_sum(1, 35, 6, 8, 9, 9, 0)
number_sum()

def dict_args_func(**kwargs):
    print(kwargs)

dict_args_func(age=56, address="Kharkiv")

#####-------------#####
def my_universal_func(name, surname, *purchases, **kwargs):
    print(name, surname, purchases, kwargs)

my_universal_func("Ihor", "Mykhailichenko", "CAr", "Bag", "apple", car_prise=4000, bag_price=400, apple=2)
