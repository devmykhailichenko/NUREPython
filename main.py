#type 'dict'
user_1 = {
    "name": "Ihor",
    "surname": "Mykh...",
    "email": "ihor@gmail.com",
}

print(
    user_1.get("name", "Unknown")
)

user_1['name'] = 'Alex'
user_1['balance'] = 10

print(user_1)

#Problem 1
products = [
    {
        "name": "Apple",
        "price": 5.00,
    },
    {
        "name": "Bread",
        "price": 10.00,
    },
]

while True:
    print("Commands: show, add, delete, exit")

    command = input("Please, type your command: ")

    match command:
        case "show":
            print("products List: \n")

            for product in products:
                print(f"{product['name']} - {product['price']} $")
        case "add":
            name = input("Please, type products name: ")
            price = float(input("Please, type products price: "))

            new_product = {
                "name": name,
                "price": price,
            }

            products.append(new_product)

            print(f"Product {name} added!")

        case "delete":
            name = input("Which product you want to delete? (type the name): ")

            for product in products:
                if product["name"] == name:
                    products.remove(product)
                    print(f"Product {name} has been removed!")
                    break
            else:
                print("Product not found!")
        case "exit":
            print("Buy-buy!")
            break
