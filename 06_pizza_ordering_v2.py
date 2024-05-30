reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]


def ordering(question, error):
    response = input(question)
    if response in reg_menu:
        return response
    elif response not in reg_menu:
        if response in gourmet_menu:
            return response
        elif response not in gourmet_menu:
            print(error)
    else:
        print(error)


# main routine here
while True:
    chosen_pizza = ordering("What pizza would you like?", "Sorry, that's not on our menu. Please try again.")
    print("You chose {}".format(chosen_pizza))
