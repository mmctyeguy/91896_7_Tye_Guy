def address_check():
    while True:
        address = input("\nWhere would you like the order delivered? ").lower()
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number is True and string is True:
            print("Your order will be delivered to {}".format(address))
            break
        else:
            print("Please enter a valid address")


def order_collect():
    while True:
        response = input("How would you like to collect your order? Pickup, or delivery?").lower()

        if response == "pickup":
            print("You have selected {}.".format(response))
            print("Our address is 111 pizza street. Please collect your order in"
                  " 30 minutes.")
            return response
        elif response == "delivery":
            print("You have selected {}.".format(response))
            print("You will be asked for your address, and a $10 delivery charge will be"
                  " added to your order.")
            extra_cost.append(10)
            extra_reason.append("Delivery Charge")
            address_check()
            return response
        else:
            print("Sorry, please choose pickup or delivery.")


# checks that the response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please try again, your response cannot be blank.")
        else:
            return response


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


extra_cost = []
extra_reason = []

while True:
    collect_method = order_collect()

    name = not_blank("What is your name?")
    print(name)
    phone_no = num_check("What is your phone number?", "Please enter a phone number", int)
    print(phone_no)
