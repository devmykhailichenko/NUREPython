import copy

# Dictionary (Словники)
person = {
    "id": 1,
    "age": 30,
    "city": "Kharkiv",
    3: "Hello",
    4.5: 10,
    (2, 3, 4): 5
}

print(person)

person_2 = dict(name="ihor", age=30, city="")

print(person_2)

print("Person id is:", person["id"])
print("Person id is:", person["city"])
print("Person id is:", person[3])
print("Person id is:", person.get("Hello"))

person_2["name"] = "Alice"
person_2["street"] = "kharkiv street"
print(person_2)

del person_2["age"]
deleted_value = person.pop(3)

print(person_2, person, deleted_value)

person_2.clear()

print(person_2)
print(person)
print("age" in person)

for key in person:
    print(person[key])

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, "-->", value)

for index, (key, value) in enumerate(person.items()):
    print(index, key, value)

# --------- copy ---------
original = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript"]
}

original_copy = original.copy()
deep_copy = copy.deepcopy(original)

original["name"] = "Alex"
original["skills"].append("Ruby")
print(original_copy, original, deep_copy)

# tuple
numbers = (1, 3, 4, 5, 3, 4, 5, 1, 1, 1, 1)
single_tuple = (5,)
# numbers[2] = 3
# del numbers[1]
print(numbers[2], type(single_tuple))

for value in numbers:
    print(value)

print(
    2 in numbers,
    len(numbers),
    max(numbers),
    numbers.count(1),
    numbers.index(1)
)

list_out_of_tuple = list(numbers)
list_out_of_tuple.append("Hello")
tuple_numbers = tuple(list_out_of_tuple)
print(type(list_out_of_tuple), list_out_of_tuple, tuple_numbers)

