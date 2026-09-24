import copy

#type 'dict'
user_1 = {
    "name": "Ihor",
    "surname": "Mykh...",
    "email": "ihor@gmail.com",
    "address": {
        "city": "Kharkiv",
        "street": "Naukova 45",
        "zip": 1035
    }
}

print(
    user_1.get("name", "Unknown")
)

user_1['name'] = 'Alex'
user_1['balance'] = 10

print(user_1)

del user_1['balance']

email = user_1.pop("email1", None)

print(user_1, email)
print("surname" in user_1)

for key, value in user_1.items():
    print(f"Value of {key} is {value}")

#######---------#######
user_copy = copy.deepcopy(user_1)
user_copy['name'] = 'Bob'
user_copy["address"]["city"] = "Kyiv"

print(f"Origin: {user_1} \n  Copy: {user_copy}")

#####------####
my_tuple = (
    1,
    2,
    3,
    3,
    3,
    [6, 7, 8] # ref -------> [6, 7, 8]
)

my_tuple[5][0] = 'Ihor'

for item in my_tuple:
    print(item)

print(my_tuple.count(3))
print(my_tuple.index(2))

#Problem example 1
# products = [
#     {
#         "name": "Apple",
#         "price": 5.00,
#     },
#     {
#         "name": "Bread",
#         "price": 10.00,
#     },
# ]
#
# while True:
#     print("Commands: show, add, delete, exit")
#
#     command = input("Please, type your command: ")
#
#     match command:
#         case "show":
#             print("products List: \n")
#
#             for product in products:
#                 print(f"{product['name']} - {product['price']} $")
#         case "add":
#             name = input("Please, type products name: ")
#             price = float(input("Please, type products price: "))
#
#             new_product = {
#                 "name": name,
#                 "price": price,
#             }
#
#             products.append(new_product)
#
#             print(f"Product {name} added!")
#
#         case "delete":
#             name = input("Which product you want to delete? (type the name): ")
#
#             for product in products:
#                 if product["name"] == name:
#                     products.remove(product)
#                     print(f"Product {name} has been removed!")
#                     break
#             else:
#                 print("Product not found!")
#         case "exit":
#             print("Buy-buy!")
#             break
