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
                       columns=['Pizza', 'Price'])
    print(tabulate(reg, showindex=False, headers=reg.columns))
    gourmet = pd.DataFrame(list(zip(gourmet_menu, gourmet_price)),
                           columns=['Pizza', 'Price'])
    print(tabulate(gourmet, showindex=False, headers=gourmet.columns))
    sides = pd.DataFrame(list(zip(sides_menu, sides_price)),
                         columns=['Item', 'Price'])
    print(tabulate(sides, showindex=False, headers=sides.columns))


# lists to hold menu items
reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]
sides_price = [14, 4, 4, 8, 9]

# main routine begins
show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    menu()
else:
    print("Program continues...")


# to do - incorporate menus & prices for all + find way to split them based on category without
# making another list
