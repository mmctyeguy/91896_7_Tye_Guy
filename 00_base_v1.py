# functions go here
# checks response is yes or no
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


# prints the instructions
def instructions():
    print('''\n\n
    **** Welcome to Pizza Place ****

    How to order:

    ** Pickup vs Delivery **
    The program will ask if you would like 
    to order delivery, or to pick up.
    If you have chosen delivery, we will need
    your name, address and phone number. 
    For pickup, we only need your name and 
    phone number, and we will provide you 
    the store's address.

    ** Choosing a Pizza **
    You will be asked if you need to look at
    the menu, and then asked to select a
    pizza from the menu. 

    ** Choosing a Side Dish **
    You will be asked if you need to look at
    the menu, and then asked to select a side
    dish from the menu.

    ** Confirming your order + Payment options **
    You will be asked for a payment type, either
    cash or credit (1.5% surcharge). Then we will
    show your full order with the total price in
    an itemised receipt. 
    You will then be asked to either confirm or 
    cancel your order, or if you need to make any 
    changes.

    **** Thanks for choosing Pizza Place! ****
        ''')


# checks the response is a number more than 0
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


# checks that the response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please try again, your response cannot be blank.")
        else:
            return response


# main routine here

ordered_before = yes_no("Have you ordered with us before?")
if ordered_before == "no":
    print(instructions())

elif ordered_before == "yes":
    print("Program continues")
