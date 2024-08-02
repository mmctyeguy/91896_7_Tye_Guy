def address_check():
    while True:
        address = input("\nWhere would you like the order delivered? ").lower()
        number = any(map(str.isdigit, address))
        string = any(map(str.isalpha, address))
        if number is True and string is True:
            print("Your order will be delivered to {}.".format(address))
            break
        else:
            print("Please enter a valid address")


while True:
    address_check()
