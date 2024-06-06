def order_collect():
    while True:
        response = input("How would you like to collect your order? Pickup, or delivery?").lower()

        if response == "pickup" or response == "delivery":
            print("You have selected {}.".format(response))
            return response
        else:
            print("Sorry, please choose pickup or delivery.")


while True:
    order_collect()
