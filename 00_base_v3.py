import pandas as pd
from tabulate import tabulate


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


# takes in data from lists, converts it to tables with custom headers and prints it
# them back out with adjusted formatting via tabulate
def menu():
    reg = pd.DataFrame(list(zip(reg_menu, reg_price)),
                       columns=['Regular Pizzas', 'Price'])
    print(tabulate(reg, showindex=False, headers=reg.columns))
    print("\n")
    gourmet = pd.DataFrame(list(zip(gourmet_menu, gourmet_price)),
                           columns=['Gourmet Pizzas', 'Price'])
    print(tabulate(gourmet, showindex=False, headers=gourmet.columns))
    print("\n")
    sides = pd.DataFrame(list(zip(sides_menu, sides_price)),
                         columns=['Add-Ons', 'Price'])
    print(tabulate(sides, showindex=False, headers=sides.columns))
    print("\n")
    bases = pd.DataFrame(list(zip(type_list, type_price)),
                         columns=['Pizza Bases', 'Price'])
    print(tabulate(bases, showindex=False, headers=bases.columns))


# counts amount of pizzas ordered
def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


# counts amount of sides ordered
def sides_counting():
    sides_counting.counter += 1
    return sides_counting.counter


# sides ordering function
def sides_ordering(question, error):
    # Function to calculate price of sides via index of lists
    def calculate_sides_price(selected_side):
        pos = sides_menu.index(selected_side)
        price = sides_price[pos]
        return price

    response = input(question).lower()
    if response == "xxx":
        return response  # Can end even with no sides ordered
    elif response in sides_menu:
        sides_counting()
        sides_order.append(response)
        print(f"You have chosen a {response}. You have {sides_counting.counter} item(s) in your basket.")
        sides_cost.append(calculate_sides_price(response))
        total_cost()
        return response
    else:
        print(error)


# pizza ordering function
def pizza_ordering(question, error):
    pizza_menu = reg_menu + gourmet_menu
    prices_list = reg_price + gourmet_price

    def base_select():
        base_type = input("What kind of base would you like for your pizza?"
                          "\n Please choose from Regular, Gluten free, Deep pan and Shallow pan")
        if base_type in type_list:
            pos = type_list.index(base_type)
            price = type_price[pos]
            extra_cost.append(price)
            extra_reason.append(base_type)
            print("You have selected a {}. This will cost ${}".format(base_type, price))
            total_cost()
            return base_type
        elif base_type not in type_list:
            print("Sorry, please select from the list.")

    # calc price of pizzas by indexing lists
    def calculate_pizza_price():
        pos = pizza_menu.index(response)
        price = prices_list[pos]
        return price

    response = input(question).lower()

    if response == "xxx":
        if pizza_counting.counter == 0:
            print("Sorry, you must order at least 1 pizza.")
        else:
            return response
    elif response in pizza_menu:
        pizza_counting()
        print("You have chosen a {}. You have {} item/s in your basket.".format(response,
                                                                                pizza_counting.counter))
        pizza_cost.append(calculate_pizza_price())
        pizza_order.append(response)
        total_cost()
        base_select()
        return response

    elif response is None:
        print(error)
    elif response in sides_menu:
        print("Sorry, that looks like it's "
              "from our sides menu. Please "
              "order a pizza first.")
    else:
        print(error)


# checks user input has numbers followed by a string (so it resembles an address)
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


# asks how user wants to collect order
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


def total_cost():
    print(f"Your total is ${sum(pizza_cost + sides_cost + extra_cost)}")


# sets counters to 0 before loop
pizza_counting.counter = 0
sides_counting.counter = 0

# lists to hold menu info
reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10.00, 12.00, 12.00, 15.00, 15.00]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [16.00, 16.00, 19.99, 19.99, 22.00]
sides_menu = ["mozzarella sticks", "l&p", "pepsi", "garlic bread", "sorbet"]
sides_price = [14.00, 3.99, 3.99, 8.00, 9.99]
type_list = ["regular", "gluten free", "deep pan", "shallow pan"]
type_price = [0.00, 0.50, 1.50, 0.50]

# lists to hold order into
pizza_order = []
sides_order = []
pizza_cost = []
sides_cost = []
extra_cost = []
extra_reason = []


# main routine here
while True:
    ordered_before = yes_no("Have you ordered with us before?")
    if ordered_before == "no":
        print(instructions())
    elif ordered_before == "yes":
        pass

    show_menu = yes_no("Would you like to see the menu?")
    if show_menu == "yes":
        menu()
        break
    else:
        break

while True:
    chosen_pizza = pizza_ordering("What pizza would you like?",
                                  "Please choose from our menu,"
                                  " or type 'xxx' to finish ordering "
                                  "off the Pizza menu.")

    if pizza_counting.counter <= 5:
        if chosen_pizza == "xxx":
            print(f"You have ordered {', '.join(pizza_order)}.")
            total_cost()
            break

    elif pizza_counting.counter >= 5:
        print("Sorry, you've reached the maximum amount of orders")
        print(f"You have ordered {', '.join(pizza_order)}.")
        total_cost()
        break

while True:
    chosen_sides = sides_ordering("What side would you like?",
                                  "Please choose from our menu or type 'xxx' to finish ordering.")

    if chosen_sides == "xxx":
        if sides_counting.counter >= 1:
            print(f"You have ordered {', '.join(sides_order)}.")
            total_cost()
            break

# Editing the order
change_order = yes_no("Would you like to make any changes?")
if change_order == "yes":
    add_remove = not_blank("Would you like to add or remove items?")
    print("")
    if add_remove == "add":
        while True:
            chosen_sides = sides_ordering("What side would you like to add?",
                                          "Please choose from our menu or type 'xxx' to finish ordering.")
            if chosen_sides == "xxx":
                print(f"You have ordered {', '.join(sides_order)}.")
                total_cost()
                break

    elif add_remove == "remove":
        while True:
            print("Your current sides order:")
            print("\n".join(sides_order))
            remove_item = input("What side would you like to remove? ").lower()

            if remove_item in sides_order:
                sides_index = sides_order.index(remove_item)
                sides_order.pop(sides_index)
                sides_cost.pop(sides_index)
                sides_counting.counter -= 1
                print(f"Removed {remove_item} from your order.")
                total_cost()
            elif remove_item == "xxx":
                break
            else:
                print("Sorry, that item is not in your order.")

else:
    print("No changes will be made.")

print("Thank you for ordering with us.")
collect_method = order_collect()

name = not_blank("What is your name?")
print(f"{name.capitalize()}.")
phone_no = num_check("What is your phone number?", "Please enter a valid phone number", int)
print(phone_no)
# Add validation for phone number length if needed

# Display final order
print("Your final order details:")
your_order_dict = {
    "Items": pizza_order + sides_order + extra_reason,
    "Price": pizza_cost + sides_cost + extra_cost
}
order_table = pd.DataFrame(your_order_dict)
print(order_table)
total_cost()
