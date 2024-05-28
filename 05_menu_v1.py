def menu():
    print("Our Menu")
    print("\nRegular Pizzas")
    for item in reg_pizzas:
        print(item)
    print("\nGourmet Pizzas")
    for item in gourmet_pizzas:
        print(item)
    print("\nSides Menu")
    for item in sides_menu:
        print(item)


reg_pizzas = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
gourmet_pizzas = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]

menu()