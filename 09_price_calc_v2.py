def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


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


def get_price():
    pos = reg_menu.index(chosen_pizza)
    price = reg_price[pos]
    return price


pizza_counting.counter = 0

reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]
sides_menu = ["mozzarella sticks", "L&P", "pepsi", "garlic bread", "sorbet"]
sides_price = [14, 4, 4, 8, 9]

pizza_order = []
order_cost = []

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
                finished = True
                break
        elif chosen_pizza in reg_menu or gourmet_menu:
            pizza_order.append(chosen_pizza)
            pizza_counting()
            print("You have chosen a {}. You have {} item/s in your basket.".format(chosen_pizza,
                                                                                    pizza_counting.counter))
            order_cost.append(get_price())
            print("Your current total is ${}".format((sum(order_cost))))
    if pizza_counting.counter >= 5:
        print("Sorry, you've reached the max amount of orders")
        finished = True
        break

while finished is True:
    print("You've ordered {}".format(pizza_order))
    print("Your total is ${}".format((sum(order_cost))))
    finished = False

