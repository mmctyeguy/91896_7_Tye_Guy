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


# lists (hold set values for testing)
pizza_cost = [9.99, 15.99]
sides_cost = [3.99, 5.99]
extra_cost = [0.00, 0.50]

processor = PaymentProcessor()

while True:
    processor.payment_type()
    processor.total_cost()
