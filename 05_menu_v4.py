import pandas as pd
from tabulate import tabulate


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
    reg = pd.DataFrame(list(zip(reg_menu, reg_price)),
                       columns=['Regular Pizzas', 'Price'])
    print(tabulate(reg, showindex=False, headers=reg.columns))
    print("\n")
    gourmet = pd.DataFrame(list(zip(gourmet_menu, gourmet_price)),
                           columns=['Gourmet Pizzas', 'Price'])
    print(tabulate(gourmet, showindex=False, headers=gourmet.columns))
    print("\n")
    sides = pd.DataFrame(list(zip(sides_menu, sides_price)),
                         columns=['Add-Ons', 'Price'])
    print(tabulate(sides, showindex=False, headers=sides.columns))


# lists to hold menu items
reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12.50, 12.50, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19.99, 19.99, 22]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]
sides_price = [14.50, 4.99, 4.99, 8, 9.99]

# main routine begins
show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    menu()
else:
    print("Program continues...")

