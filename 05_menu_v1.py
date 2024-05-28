
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


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

show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    print(menu())
else:
    print("Program continues...")