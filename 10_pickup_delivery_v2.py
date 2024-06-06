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
    if collect_method == "delivery":
        extra_cost.append(10)
        extra_reason.append("Delivery Charge")


# plan
# if pickup, go to ask name + phone number
# if delivery, do that + ask address + add charge to order
# calculate time for order (pickup i.e it will be ready in... delivery it will arrive in...)
# use datetime?