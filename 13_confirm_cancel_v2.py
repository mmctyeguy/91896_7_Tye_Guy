def confirm_order():
    while True:
        confirm = yes_no("Would you like to confirm your  order? (yes/no) ")
        if confirm == 'no':
            print("Your order has been cancelled.")
            exit()  # Exit the program if the user cancels the order
        elif confirm == 'yes':
            return
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")