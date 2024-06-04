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


# checks if response is on the pizza menus
def pizza_ordering(question, error):
    response = input(question).lower()
    pizza_menu = reg_menu + gourmet_menu

    if response is None:
        print(error)
    elif response in pizza_menu:
        pizza_order.append(response)
        pizza_counting()
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                pizza_counting.counter))
        return response
    elif response == "xxx":
        return response
    elif response in sides_menu:
        print("Sorry, that looks like it's "
              "from our sides menu. Please "
              "order a pizza first.")
    else:
        print(error)


# counts amount of pizzas ordered
def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


# counts amount of sides ordered
def sides_counting():
    sides_counting.counter += 1
    return sides_counting.counter


# checks if response is on the menu
def sides_ordering(question, error):
    response = input(question).lower()

    if response is None:
        print(error)
    elif response == "xxx":
        return response
    elif response in sides_menu:
        sides_order.append(response)
        sides_counting()
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                sides_counting.counter))
        return response
    else:
        print(error)


pizza_counting.counter = 0
sides_counting.counter = 0

reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "l&p", "pepsi", "garlic bread", "sorbet"]
sides_price = [14, 4, 4, 8, 9]


pizza_order = []
sides_order = []

your_order_dict = {
    "Pizzas": pizza_order,
    "Sides": sides_order}

# main routine begins

while True:
    ordered_before = yes_no("Have you ordered with us before?")
    if ordered_before == "no":
        print(instructions())

    elif ordered_before == "yes":
        pass

    show_menu = yes_no("Would you like to see the menu?")
    if show_menu == "yes":
        menu()
    else:
        break

# main routine here
while True:
    chosen_pizza = pizza_ordering("What pizza would you like?", "Please choose from our menu, or type"
                                                                " 'xxx' to finish ordering off "
                                                                "the Pizza menu.")

    if pizza_counting.counter <= 5:
        if chosen_pizza == "xxx":
            if pizza_counting.counter <= 0:
                print("Sorry, you must order at least 1 pizza.")
            else:
                print(pizza_order)
                break

    elif pizza_counting.counter >= 5:
        print("Sorry, you've reached the max amount of orders")
        print(pizza_order)
        break

while True:
    chosen_sides = sides_ordering("What side would you like?", "Please choose from our menu or type "
                                                               "'xxx' to finish ordering.")
    if sides_counting.counter <= 0:
        if chosen_sides == "xxx":
            print("You have chosen {} sides.".format(sides_counting.counter))
            break
    elif sides_counting.counter >= 0:
        if chosen_sides == "xxx":
            print(sides_order)
            break


print("Here is your receipt")
print(your_order_dict)
