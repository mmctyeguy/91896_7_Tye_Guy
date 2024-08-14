def payment_type():
    payment_method = input("Please select your payment method. Cash or credit? (ca/cr) ")
    if payment_method in ["cash", "ca"]:
        print("You have selected cash as your payment type.")
        return "cash"
    elif payment_method in ["credit", "cr"]:
        print("You have selected credit as your payment type.\n"
              "Please be aware that there is a 15% surcharge for credit.")
        extra_reason.append("credit surcharge")
        return "credit"
    else:
        print("Invalid selection. Please choose 'cash' or 'credit'.")
        return payment_type()  # Recursive call for a valid input


def total_cost(pizza_price, sides_price, extra_price, payment_method):
    # Calculate the sum of lists
    total = sum(pizza_price) + sum(sides_price) + sum(extra_price)

    # Apply surcharge if payment method is credit
    if payment_method == "credit":
        surcharge = total * 0.15
        total += surcharge

    return total


# Example usage
pizza_cost = [9.99]
sides_cost = [3.99]
extra_cost = [10.00]
extra_reason = ["delivery"]

# Get payment method from user
method = payment_type()

# Calculate and display the final total
final_total = total_cost(pizza_cost, sides_cost, extra_cost, method)
print(f"Your final total is: ${final_total:.2f}")



