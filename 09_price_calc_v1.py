import pandas as pd
from tabulate import tabulate


# counts amount of pizzas ordered
def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


# counts amount of sides ordered
def sides_counting():
    sides_counting.counter += 1
    return sides_counting.counter


# checks that the response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Please try again, your response cannot be blank.")
        else:
            return response


def pizza_ordering(question, error):
    response = input(question).lower()
    if response == "xxx":
        return response
    elif response in reg_menu:
        return response
    else:
        if response in gourmet_menu:
            return response
        else:
            if response in sides_menu:
                print("Sorry, that looks like it's "
                      "from our sides menu. Please "
                      "order a pizza first.")
            else:
                print(error)


def sides_ordering(question, error):
    response = input(question).lower()
    if response == "xxx":
        return response
    elif response in sides_menu:
        return response
    else:
        print(error)


# main routine starts here
pizza_counting.counter = 0
sides_counting.counter = 0

reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]
sides_price = [14, 4, 4, 8, 9]

pizza_order = []
sides_order = []

order_dict = {
    "Pizza": pizza_order,
    "Sides": sides_order
}

# goal - start off with a set order and using the lists calculate the price
# then move to making it work for any order

chosen_pizza = "cheese"
chosen_sides = "mozzarella sticks"

pizza_order.append(chosen_pizza)
sides_order.append(chosen_sides)

order_frame = pd.DataFrame(order_dict)

pos = reg_menu.index(chosen_pizza)
price = reg_price[pos]

print(pizza_order, price)






