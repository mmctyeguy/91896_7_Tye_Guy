import pandas as pd
from tabulate import tabulate

# Functions


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer 'yes' or 'no'.")


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


def num_check(question, error, num_type):
    while True:
        try:
            response = num_type(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


def not_blank(question):
    while True:
        response = input(question)
        if response.strip():
            return response
        else:
            print("Response cannot be blank.")


def menu():
    reg = pd.DataFrame(list(zip(reg_menu, reg_price)), columns=['Regular Pizzas', 'Price'])
    print(tabulate(reg, showindex=False, headers=reg.columns))
    print("\n")
    gourmet = pd.DataFrame(list(zip(gourmet_menu, gourmet_price)), columns=['Gourmet Pizzas', 'Price'])
    print(tabulate(gourmet, showindex=False, headers=gourmet.columns))
    print("\n")
    sides = pd.DataFrame(list(zip(sides_menu, sides_price)), columns=['Add-Ons', 'Price'])
    print(tabulate(sides, showindex=False, headers=sides.columns))
    print("\n")
    bases = pd.DataFrame(list(zip(type_list, type_price)), columns=['Pizza Bases', 'Price'])
    print(tabulate(bases, showindex=False, headers=bases.columns))
    print("\n")


def pizza_counting():
    pizza_counting.counter += 1
    return pizza_counting.counter


def sides_counting():
    sides_counting.counter += 1
    return sides_counting.counter


def order_counting():
    order_counting.counter += 1
    return order_counting.counter


def sides_ordering(question, error):
    def calculate_sides_price(selected_side):
        return sides_price[sides_menu.index(selected_side)]

    response = input(question).lower()
    if response == "xxx":
        return response
    elif response in sides_menu:
        sides_counting()
        sides_order.append(response)
        sides_cost.append(calculate_sides_price(response))
        print(f"You have chosen a {response}. You have {sides_counting.counter} item(s) in your basket.")
        processor.total_cost()
        return response
    else:
        print(error)


def pizza_ordering(question, error):
    pizza_menu = reg_menu + gourmet_menu
    prices_list = reg_price + gourmet_price

    def base_select():
        while True:
            base_type = input("What kind of base would you like for your pizza?"
                              "\n (Regular, Gluten free, Deep pan, Shallow pan) ")
            if base_type in type_list:
                price = type_price[type_list.index(base_type)]
                extra_cost.append(price)
                extra_reason.append(base_type)
                print(f"You have selected {base_type}. This will cost ${price:.2f}")
                return base_type
            else:
                print("Sorry, please select from the list.")
                # bug here for some reason you can skip base selection...

    def calculate_pizza_price():
        return prices_list[pizza_menu.index(response)]

    response = input(question).lower()
    if response == "xxx":
        if pizza_counting.counter == 0:
            print("Sorry, you must order at least 1 pizza.")
        else:
            return response
    elif response in pizza_menu:
        pizza_counting()
        pizza_order.append(response)
        pizza_cost.append(calculate_pizza_price())
        print(f"You have chosen a {response}. You have {pizza_counting.counter} item(s) in your basket.")
        base_select()
        processor.total_cost()
        return response
    elif response in sides_menu:
        print("Sorry, that looks like it's from our sides menu. Please order a pizza first.")
    else:
        print(error)


def confirm_order():
    while True:
        confirm = yes_no("Would you like to confirm your order? (yes/no) ")
        if confirm == 'no':
            print("Your order has been cancelled.")
            exit()  # Exit the program if the user cancels the order
        elif confirm == 'yes':
            return
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")


def address_check():
    while True:
        address = input("\nWhere would you like the order delivered? ").lower()
        if any(char.isdigit() for char in address) and any(char.isalpha() for char in address):
            print(f"Your order will be delivered to {address}.")
            break
        else:
            print("Please enter a valid address")


def order_collect():
    while True:
        response = input("How would you like to collect your order? (Pickup/Delivery) ").lower()
        if response == "pickup":
            print(f"You have selected {response}.")
            print("Our address is 111 Pizza Street. Please collect your order in 30 minutes.")
            return response
        elif response == "delivery":
            print(f"You have selected {response}.")
            print("You will be asked for your address, and a $10 delivery charge will be added to your order.")
            extra_cost.append(10)
            extra_reason.append("Delivery Charge")
            address_check()
            return response
        else:
            print("Sorry, please choose pickup or delivery.")


def write_order_to_file(name, order_number):
    filename = f"{name.lower()}_order_{order_number}.txt"
    with open(filename, 'w') as file:
        file.write("**** Order Summary for {} ****\n\n".format(name))
        file.write("Items Ordered:\n")
        for item, price in zip(pizza_order + sides_order + extra_reason, pizza_cost + sides_cost + extra_cost):
            file.write(f"{item.capitalize()}: ${price:.2f}\n")
        file.write("\n")
        total = processor.total_cost()
        file.write(f"Total Cost: ${total:.2f}\n")
    print(f"Order details have been saved to {filename}.")


class PaymentProcessor:
    def __init__(self):
        self.payment_method = None

    def payment_type(self):
        self.payment_method = input("Please select your payment method. Cash or credit? (ca/cr) ").lower()
        if self.payment_method in ["cash", "ca"]:
            print("You have selected cash as your payment type.")
            self.payment_method = "cash"
        elif self.payment_method in ["credit", "cr"]:
            print("You have selected credit as your payment type.\n"
                  "Please be aware that there is a 15% surcharge for credit.")
            self.payment_method = "credit"
        else:
            print("Invalid selection. Please choose 'cash' or 'credit'.")
            self.payment_type()  # Recursive call for a valid input

    def total_cost(self):
        total = sum(pizza_cost) + sum(sides_cost) + sum(extra_cost)
        if self.payment_method == "credit":
            surcharge = total * 0.15
            total += surcharge
        print(f"Your total is ${total:.2f}")
        return total


class OrderManager:
    def __init__(self):
        self.processor = PaymentProcessor()

    def edit_order(self):
        while True:
            edit = yes_no("Do you want to edit your order? (yes/no) ")
            if edit == 'no':
                print("No changes will be made.")
                break
            elif edit == 'yes':
                self.modify_order()
                break
            else:
                print("Invalid response. Please answer 'yes' or 'no'.")

    def modify_order(self):
        while True:
            action = input("Would you like to add or remove items? (add/remove/xxx) ").lower()
            if action == 'add':
                self.modify_items('add')
            elif action == 'remove':
                self.modify_items('remove')
            elif action == 'xxx':
                break
            else:
                print("Invalid choice. Please enter 'add', 'remove', or 'xxx'.")

    def modify_items(self, action):
        while True:
            category = input("Which category would you like to edit? (pizza/sides/xxx) ").lower()
            if category in ['pizza', 'sides']:
                if action == 'add':
                    self.add_item(category)
                elif action == 'remove':
                    self.remove_item(category)
            elif category == 'xxx':
                break
            else:
                print("Invalid category. Please enter 'pizza' or 'sides'.")

    @staticmethod
    # because it's only called in the class and doesn't need access to anything else
    def add_item(category):
        if category == 'pizza':
            pizza_ordering("What pizza would you like to add? ", "Please choose from our menu.")
        elif category == 'sides':
            sides_ordering("What side would you like to add? ", "Please choose from our menu.")

    def remove_item(self, category):
        if category == 'pizza':
            print("Your current pizza order:")
            print("\n".join(pizza_order))
            item = input("Which pizza would you like to remove? ").lower()
            if item in pizza_order:
                if pizza_counting.counter > 1:
                    self.remove_from_order(item, pizza_order, pizza_cost)
                    pizza_counting.counter -= 1
                elif pizza_counting.counter <= 1:
                    print("Sorry, you must order at least 1 pizza.")
            elif item == "xxx":
                pass
            else:
                print("Sorry, that item isn't in your order.")
        elif category == 'sides':
            print("Your current sides order:")
            print("\n".join(sides_order))
            item = input("Which side would you like to remove? ").lower()
            if item in sides_order:
                self.remove_from_order(item, sides_order, sides_cost)
                sides_counting.counter -= 1
            elif item == "xxx":
                pass
            else:
                print("Sorry, that item isn't in your order.")

    def remove_from_order(self, item, order_list, cost_list):
        index = order_list.index(item)
        order_list.pop(index)
        cost_list.pop(index)
        print(f"{item} has been removed.")
        self.processor.total_cost()

    def finalize_order(self):
        name = not_blank("Please enter your name: ")
        order_counting()
        order_number = order_counting.counter
        write_order_to_file(name, order_number)
        self.processor.payment_type()
        confirm_order()


# Global Variables

reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [9.99, 11.99, 11.99, 14.99, 14.99]
gourmet_menu = ["americano", "margherita", "supreme", "capricciosa", "shrimp"]
gourmet_price = [15.99, 15.99, 19.99, 19.99, 21.99]
sides_menu = ["mozzarella sticks", "l&p", "pepsi", "garlic bread", "sorbet", "chips"]
sides_price = [13.99, 3.99, 3.99, 7.99, 9.99, 5.99]
type_list = ["regular", "gluten free", "deep pan", "shallow pan"]
type_price = [0.00, 0.50, 1.50, 0.50]

pizza_order = []
sides_order = []
pizza_cost = []
sides_cost = []
extra_cost = []
extra_reason = []

pizza_counting.counter = 0
sides_counting.counter = 0
order_counting.counter = 0  # Track order counts to avoid overwriting files

# Main Routine

while True:
    processor = PaymentProcessor()
    manager = OrderManager()

    while True:
        ordered_before = yes_no("Have you ordered with us before? (yes/no) ")
        if ordered_before == "no":
            instructions()

        show_menu = yes_no("Would you like to see the menu? (yes/no) ")
        if show_menu == "yes":
            menu()

        break

    while True:
        chosen_pizza = pizza_ordering("What pizza would you like to order? (or type 'xxx' to finish) ",
                                      "Please choose from our menu, or type 'xxx' to finish ordering.")

        if chosen_pizza == "xxx" and pizza_counting.counter > 0:
            print(f"You have ordered {', '.join(pizza_order)}.")
            processor.total_cost()
            break
        elif pizza_counting.counter >= 5:
            print("Sorry, you've reached the maximum amount of orders")
            print(f"You have ordered {', '.join(pizza_order)}.")
            processor.total_cost()
            break

    while True:
        chosen_sides = sides_ordering("What side would you like to order? (or type 'xxx' to finish) ",
                                      "Please choose from our menu or type 'xxx' to finish ordering.")

        if chosen_sides == "xxx":
            if sides_counting.counter > 0:
                print(f"You have ordered {', '.join(sides_order)}.")
            break

    manager.edit_order()
    print("Thank you for ordering with us.")
    collect_method = order_collect()

    processor.total_cost()

    phone_no = num_check("What is your phone number? ", "Please enter a valid phone number", int)
    print(f"Phone Number: 0{phone_no}")

    manager.finalize_order()

    # Display final order
    print("Your final order details:")
    your_order_dict = {
        "Items": pizza_order + sides_order + extra_reason,
        "Price": pizza_cost + sides_cost + extra_cost
    }

    processor.total_cost()
    order_table = pd.DataFrame(your_order_dict)
    print(order_table)

    # Ask if the user wants to make another order
    new_order = yes_no("Would you like to make another order? (yes/no) ")
    if new_order == "no":
        print("Thank you for visiting Pizza Place! Have a great day!")
        break
    else:
        # Reset variables for a new order
        pizza_order.clear()
        sides_order.clear()
        pizza_cost.clear()
        sides_cost.clear()
        extra_cost.clear()
        extra_reason.clear()
        pizza_counting.counter = 0
        sides_counting.counter = 0
