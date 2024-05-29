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


# lists to hold menu items
menu_list = [["cheese", 10], ["pepperoni", 12], ["hawaiian", 12], ["meatball", 15], ["vegetarian", 15]]
gourmet_pizzas = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]

df = pandas.DataFrame(menu_list, columns=['Pizza', 'Price'])

show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    print(df)
else:
    print("Program continues...")

# to do - incorporate menus & prices for all + find way to split them based on category without
# making another list
