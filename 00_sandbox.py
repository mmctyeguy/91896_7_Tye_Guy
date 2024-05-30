import pandas as pd
from tabulate import tabulate


# functions go here
# checks response is yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


# prints the instructions
def instructions():
    print('''\n\n
    **** Welcome to Pizza Place ****

    How to order:

    ** Pickup vs Delivery **
    The program will ask if you would like 
    to order delivery, or to pick up.
    If you have chosen delivery, we will need
    your name, address and phone number. 
    For pickup, we only need your name and 
    phone number, and we will provide you 
    the store's address.

    ** Choosing a Pizza **
    You will be asked if you need to look at
    the menu, and then asked to select a
    pizza from the menu. 

    ** Choosing a Side Dish **
    You will be asked if you need to look at
    the menu, and then asked to select a side
    dish from the menu.

    ** Confirming your order + Payment options **
    You will be asked for a payment type, either
    cash or credit (1.5% surcharge). Then we will
    show your full order with the total price in
    an itemised receipt. 
    You will then be asked to either confirm or 
    cancel your order, or if you need to make any 
    changes.

    **** Thanks for choosing Pizza Place! ****
        ''')


# checks the response is a number more than 0
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that the response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please try again, your response cannot be blank.")
        else:
            return response


# takes in data from lists, converts it to tables with custom headers and prints
# them back out with adjusted formatting via tabulate
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


# counting for the amount of items in order
def counting():
    counting.counter += 1
    return counting.counter


# checks response is on the menu, returns response
def ordering(question, error):
    response = input(question).lower()
    if response in reg_menu:
        return response
    elif response not in reg_menu:
        if response in gourmet_menu:
            return response
        elif response not in gourmet_menu:
            print(error)


counting.counter = 0

# lists to hold menu items
reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]
sides_price = [14, 4, 4, 8, 9]

# main routine begins


ordered_before = yes_no("Have you ordered with us before?")
if ordered_before == "no":
    print(instructions())
else:
    pass

show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    menu()

while True:
    chosen_pizza = ordering("What pizza would you like?", "Sorry, that's not on our menu. Please try again.")
    if counting.counter <= 5:
        if chosen_pizza is None:
            pass
        elif chosen_pizza in reg_menu or gourmet_menu:
            counting()
            print("You have chosen a {}. You have {} item/s in your basket.".format(chosen_pizza, counting.counter))
        if counting.counter >= 5:
            print("Sorry, you've reached the max amount of orders")
            break

