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


# counts amount of pizzas ordered
def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


# counts amount of sides ordered
def sides_counting():
    sides_counting.counter += 1
    return sides_counting.counter


# sides ordering function
def sides_ordering(question, error):
    # calc price of sides via index of lists
    def sides():
        pos = sides_menu.index(response)
        price = sides_price[pos]
        return price

    response = input(question).lower()
    if response == "xxx":
        return response  # can end even with no sides ordered
    elif response in sides_menu:
        sides_counting.counter += 1
        sides_order.append(response)
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                sides_counting.counter))
        sides_cost.append(sides())
        print("Your current total is ${}".format((sum(sides_cost + pizza_cost))))
        return response
    else:
        print(error)


# pizza ordering function
def pizza_ordering(question, error):
    pizza_menu = reg_menu + gourmet_menu
    prices_list = reg_price + gourmet_price

    # calc price of pizzas by indexing lists
    def pizza_price():
        pos = pizza_menu.index(response)
        price = prices_list[pos]
        return price

    response = input(question).lower()

    if response == "xxx":
        if pizza_counting.counter == 0:
            print("Sorry, you must order at least 1 pizza.")
        else:
            return response
    elif response in pizza_menu:
        pizza_counting()
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                pizza_counting.counter))
        pizza_cost.append(pizza_price())
        pizza_order.append(response)
        print("Your current total is ${}".format((sum(pizza_cost))))
        return response
    elif response is None:
        print(error)
    elif response in sides_menu:
        print("Sorry, that looks like it's "
              "from our sides menu. Please "
              "order a pizza first.")
    else:
        print(error)


# sets counters to 0 before loop
pizza_counting.counter = 0
sides_counting.counter = 0

# lists to hold menu info
reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "l&p", "pepsi", "garlic bread", "sorbet"]
sides_price = [14, 4, 4, 8, 9]

# lists to hold order into
pizza_order = []
sides_order = []
pizza_cost = []
sides_cost = []

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
    chosen_pizza = pizza_ordering("What pizza would you like?",
                                  "Please choose from our menu,"
                                  " or type 'xxx' to finish ordering "
                                  "off the Pizza menu.")

    if pizza_counting.counter <= 5:
        if chosen_pizza == "xxx":
            print("You have ordered {}.".format(pizza_order))
            print("Your total is ${}".format(sum(pizza_cost)))
            break

    elif pizza_counting.counter >= 5:
        print("Sorry, you've reached the max amount of orders")
        print("You have ordered {}.".format(pizza_order))
        print("Your total is ${}".format(sum(pizza_cost)))
        break

while True:
    chosen_sides = sides_ordering("What side would you like?", "Please choose from our menu or type "
                                                               "'xxx' to finish ordering.")
    if chosen_sides == "xxx":
        if sides_counting.counter >= 1:
            print("You have ordered {}.".format(sides_order))
        print("Your total is ${}".format(sum(sides_cost + pizza_cost)))
        finished = True
        break

while finished is True:

    # dict to organise order info
    your_order_dict = {
        "Items": pizza_order + sides_order,
        "Price": pizza_cost + sides_cost
    }

    order_table = pd.DataFrame(your_order_dict)
    print(order_table)
    print("Your current total is ${}".format((sum(sides_cost + pizza_cost))))
    finished = False





