def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ["yes", "y"]:
            return "yes"
        elif response in ["no", "n"]:
            return "no"
        else:
            print("Please answer 'yes' or 'no'.")


def not_blank(question):
    while True:
        response = input(question)
        if response.strip():
            return response
        else:
            print("Response cannot be blank.")


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

    def finalize_order(self):
        name = not_blank("Please enter your name: ")
        order_counting()
        order_number = order_counting.counter
        write_order_to_file(name, order_number)
        self.processor.payment_type()
        confirm_order()


def order_counting():
    order_counting.counter += 1
    return order_counting.counter


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


pizza_cost = [9.99, 15.99]
sides_cost = [3.99, 5.99]
extra_cost = [0.00, 0.50, 10]
pizza_order = ["cheese", "americano"]
sides_order = ["l&p", "chips"]
extra_reason = ["regular", "gluten free", "delivery charge"]

order_counting.counter = 0  # Track order counts to avoid overwriting files

processor = PaymentProcessor()
manager = OrderManager()

while True:
    manager.finalize_order()
