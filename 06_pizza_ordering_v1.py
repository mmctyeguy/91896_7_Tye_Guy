reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16, 15, 19, 19, 22]

while True:
    pizza1 = input("What pizza would you like?")
    if pizza1 in reg_menu:
        print("You have chosen {}".format(pizza1))
    elif pizza1 in gourmet_menu:
        print("You have chosen {}".format(pizza1))
    else:
        print("Sorry, please order off the menu.")

