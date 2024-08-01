def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


def confirm_order():
    confirm = yes_no("Do you want to confirm your order?")
    if confirm == 'no':
        print("Order canceled.")
        # Logic to allow user to make changes or restart
    elif confirm == 'yes':
        print("Order confirmed.")
