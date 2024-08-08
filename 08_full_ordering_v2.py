import pandas as pd


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


pizza_counting.counter = 0
sides_counting.counter = 0

reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "l&p", "pepsi", "garlic bread", "sorbet", "chips"]
sides_price = [14, 4, 4, 8, 9, 5]

pizza_order = []
sides_order = []

your_order_dict = {
    "Pizzas": pizza_order,
    "Sides": sides_order}

your_order_frame = pd.DataFrame(your_order_dict)

# main routine here
while True:
    chosen_pizza = pizza_ordering("What pizza would you like?", "Please choose from our menu, or type"
                                                                " 'xxx' to finish ordering off the Pizza menu.")
    if pizza_counting.counter <= 5:
        if chosen_pizza is None:
            pass
        elif chosen_pizza == "xxx":
            if pizza_counting.counter <= 0:
                print("Sorry, you must order at least 1 pizza.")
            elif pizza_counting.counter >= 0:
                print(pizza_order)
                break
        elif chosen_pizza in reg_menu or gourmet_menu:
            pizza_order.append(chosen_pizza)
            pizza_counting()
            print("You have chosen a {}. You have {} item/s in your basket.".format(chosen_pizza, pizza_counting.counter))
    if pizza_counting.counter >= 5:
        print("Sorry, you've reached the max amount of orders")
        print(pizza_order)
        break
    else:
        continue

while True:
    chosen_sides = sides_ordering("What side would you like?", "Please choose from our menu or type "
                                                               "'xxx' to finish ordering.")
    if chosen_sides not in sides_menu:
        if sides_counting.counter <= 0:
            if chosen_sides is None:
                pass
            elif chosen_sides == "xxx":
                print("You have chosen {} sides.".format(sides_counting.counter))
                break
        elif sides_counting.counter >= 0:
            if chosen_sides is None:
                pass
            elif chosen_sides == "xxx":
                print(sides_order)
                break
    elif chosen_sides in sides_menu:
        sides_order.append(chosen_sides)
        sides_counting()
        print("You have chosen a {}. You have {} item/s in your basket.".format(chosen_sides, sides_counting.counter))
