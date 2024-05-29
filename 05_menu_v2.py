import pandas


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


# lists to hold menu items
reg_pizzas = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
price = [10, 12, 12, 15, 15]

df = pandas.DataFrame(list(zip(reg_pizzas, price)),
                      columns=['Pizza', 'Price'])

show_menu = yes_no("Would you like to see the menu?")
if show_menu == "yes":
    print(df)
else:
    print("Program continues...")

