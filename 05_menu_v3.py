import pandas


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
    # lists to hold menu items
    menu_list_reg = [["cheese", 10], ["pepperoni", 12], ["hawaiian", 12], ["meatball", 15], ["vegetarian", 15]]
    menu_list_gourmet = [["americano", 19], ["margherita", 16], ["supreme", 18], ["capricciosa", 22], ["shrimp", 19]]
    menu_list_sides = [["mozzarella sticks", 14], ["L&P", 4], ["pepsi", 4], ["garlic bread", 8], ["sorbet", 9]]

    reg = pandas.DataFrame(menu_list_reg, columns=['Pizza', 'Price'])
    gourmet = pandas.DataFrame(menu_list_gourmet, columns=['Pizza', 'Price'])
    sides = pandas.DataFrame(menu_list_sides, columns=['Item', 'Price'])

    print(reg)
    print(gourmet)
    print(sides)


show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    menu()
else:
    print("Program continues...")

# to do - incorporate menus & prices for all + find way to split them based on category without
# making another list
