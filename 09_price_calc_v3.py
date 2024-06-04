def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


# counts amount of sides ordered
def sides_counting():
    sides_counting.counter += 1
    return sides_counting.counter


def sides_ordering(question, error):

    def sides():
        pos = sides_menu.index(response)
        price = sides_price[pos]
        return price

    response = input(question).lower()
    if response == "xxx":
        return response
    elif response in sides_menu:
        sides_counting.counter += 1
        sides_order.append(response)
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                sides_counting.counter))
        order_cost.append(sides())
        print("Your current total is ${}".format((sum(order_cost))))
        return response
    else:
        print(error)


# checks if response is on the pizza menus
def pizza_ordering(question, error):
    pizza_menu = reg_menu + gourmet_menu
    prices_list = reg_price + gourmet_price

    def pizza_price():
        pos = pizza_menu.index(response)
        price = prices_list[pos]
        return price

    response = input(question).lower()

    if response is None:
        print(error)
    elif response in pizza_menu:
        pizza_order.append(response)
        pizza_counting()
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                pizza_counting.counter))
        order_cost.append(pizza_price())
        print("Your current total is ${}".format((sum(order_cost))))
        return response
    elif response == "xxx":
        return response
    elif response in sides_menu:
        print("Sorry, that looks like it's "
              "from our sides menu. Please "
              "order a pizza first.")
    else:
        print(error)


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
order_cost = []

your_order_dict = {
    "Pizzas": pizza_order,
    "Sides": sides_order}


# main routine here
while True:
    chosen_pizza = pizza_ordering("What pizza would you like?",
                                  "Please choose from our menu,"
                                  " or type 'xxx' to finish ordering "
                                  "off the Pizza menu.")

    if pizza_counting.counter <= 5:
        if chosen_pizza == "xxx":
            if pizza_counting.counter <= 0:
                print("Sorry, you must order at least 1 pizza.")
            else:
                print(pizza_order)
                finished = True
                break

    elif pizza_counting.counter >= 5:
        print("Sorry, you've reached the max amount of orders")
        print(pizza_order)
        finished = True
        break

while True:
    chosen_sides = sides_ordering("What side would you like?", "Please choose from our menu or type "
                                                               "'xxx' to finish ordering.")
    if sides_counting.counter <= 0:
        if chosen_sides == "xxx":
            print("You have chosen {} sides.".format(sides_counting.counter))
            finished = True
            break
    elif sides_counting.counter >= 0:
        if chosen_sides == "xxx":
            print(sides_order)
            finished = True
            break

while finished is True:
    print("You've ordered {}".format(your_order_dict))
    print("Your total is ${}".format((sum(order_cost))))
    finished = False

