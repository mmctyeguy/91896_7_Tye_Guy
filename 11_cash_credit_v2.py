# Define the currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Define the total_cost function
def total_cost():
    # Calculate the total cost by summing up the elements of the lists
    total = sum(pizza_cost) + sum(sides_cost) + sum(extra_cost)

    # Format the total using the currency function
    formatted_total = currency(total)

    # Print the formatted total
    print(f"Your total is {formatted_total}")


def payment_type():
    payment_method = input("please select your payment method. Cash or credit? (ca/cr)")
    if payment_method == "cash" or payment_method == "ca":
        print("You have selected cash as your payment type")
        return "cash"
    elif payment_method == "credit" or payment_method == "cr":
        print("You have selected credit as your payment type.\n"
              " Please be aware that there is a 15% surcharge for credit.")
        extra_reason.append("credit surcharge")
        return "credit"


pizza_cost = [9.99]
sides_cost = [3.99]
extra_cost = [10.00]
extra_reason = ["delivery"]


