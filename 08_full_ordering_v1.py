def counting():
    counting.counter += 1
    return counting.counter


# checks that the response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please try again, your response cannot be blank.")
        else:
            return response


def ordering(question, error):
    response = input(question).lower()
    if response == "xxx":
        return response
    elif response in reg_menu:
        return response
    elif response not in reg_menu:
        if response in gourmet_menu:
            return response
        elif response not in gourmet_menu:
            print(error)


counting.counter = 0

reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]

your_order = []

# main routine here
while True:
    chosen_pizza = ordering("What pizza would you like?", "Please choose from our menu, or type"
                                                          " 'xxx' to finish ordering off the Pizza menu.")
    if counting.counter <= 5:
        if chosen_pizza is None:
            pass
        elif chosen_pizza == "xxx":
            if counting.counter <= 0:
                print("Sorry, you must order at least 1 pizza.")
            elif counting.counter >= 0:
                print([your_order])
                break
        elif chosen_pizza in reg_menu or gourmet_menu:
            your_order.append(chosen_pizza)
            counting()
            print("You have chosen a {}. You have {} item/s in your basket.".format(chosen_pizza, counting.counter))
    if counting.counter >= 5:
        print("Sorry, you've reached the max amount of orders")
        break
    else:
        continue


print("done")
