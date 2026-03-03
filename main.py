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