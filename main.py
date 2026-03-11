# Functions
# __code__
# __globals__
# __defaults__
# __name__
# __annotations__
# __closure__
print(__name__)

# L - local, E - Enclosing, G - global, B - Built-in

def say_hello():
    print("Hello")

say_hello()

def greet(name):
    print(f"Hello {name}")

greet("Ihor")

def add(a, b=0):
    return a + b

print(add(1))

# Keyword arguments
print(
    add(b=5, a=3)
)

lambda_add = lambda a, b: a + b

print(lambda_add(5, 6))

numbers = [1, 2, 3, 5, 6]

print(
    list(map(lambda item: item ** 2, numbers))
)

# input
result = input("Please provide a number:")
result_number = int(result)
print(result, type(result), result_number, type(result_number))

# Task
def print_menu():
    print("==== Budget Tracker ====")
    print("1. Додати витрату")
    print("2. Показати всі витрати")
    print("3. Статистика")
    print("4. Вийти")

def add_expenses(expenses):
    amount = float(input("Сума витрати: "))
    category = input("Категорія (food, car, taxi...)")
    description = input("Опис (коротко):")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

def show_expenses(expenses):
    if len(expenses) == 0:
        print("Поки що ви не зробили ніяких витрат...")
        return

    print("---- Всі витрати ----")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}: {expense['amount']:} EUR | {expense['category']} | {expense['description']}")


def build_category_totals(expenses):
    totals = {}

    for e in expenses:
        cat = e["category"]
        amount = e["amount"]

        if cat not in totals:
            totals[cat] = 0.0

        totals[cat] += amount

    return totals


def show_statistics(expenses):
    if len(expenses) == 0:
        print("Немає даних!")
        return

    total_spent = 0.0
    for e in expenses:
        total_spent += e["amount"]

    category_totals = build_category_totals(expenses)

    print("----Statistics----")
    print(f"Overall spendings: {total_spent} EUR")

    for cat, amount in category_totals.items():
        print(f"–{cat}: {amount} EUR")


def budget_tracker():
    expenses = []

    while True:
        print_menu()
        choice = input("Ваш вибір (1-4): ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_statistics(expenses)
        elif choice == "4":
            print("До зустрічі!")
            break
        else:
            print("Невірний вибір! Введіть від 1 до 4х...")

budget_tracker()

# Function syntax

def greet(name, age=30):
    print(f"Hello, {name}, you are {age} years")

greet("John")

def add_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list


print(add_item(5))
print(add_item(10))

numbers = [3, 4, 5]
print(*numbers)

data = {"name": "Bob", "age": 56}
print({
    **data,
    "city": "New York"
})

# *args **kwargs
def my_f(operation="+", *args):
    match operation:
        case "+":
            print(sum(args))
    print("My f", args)

my_f("+", 2, 3, 4, 5, 1000, 11)

def my_kwargs(normal_1, normal_2, *args, **kwargs):
    print(normal_1, normal_2, args, kwargs) # {'name': 'Alex', 'isAdmin': True, 'age': 56}

my_kwargs(1, 2, 3, 4, 5, 6, 7, name="Alex", isAdmin=True, age=56)

