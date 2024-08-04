def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer 'yes' or 'no'.")


def confirm_order():
    while True:
        confirm = yes_no("Would you like to confirm your  order? (yes/no) ")
        if confirm == 'no':
            print("Your order has been cancelled.")
            exit()  # Exit the program if the user cancels the order
        elif confirm == 'yes':
            print("Order confirmed.")
            return
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")


while True:
    confirm_order()
