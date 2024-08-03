def write_order_to_file(name):
    filename = f"{name.lower()}_order.txt"
    with open(filename, 'w') as file:
        file.write("**** Order Summary ****\n\n")
        file.write("Items Ordered:\n")
        for item, price in zip(pizza_order + sides_order + extra_reason, pizza_cost + sides_cost + extra_cost):
            file.write(f"{item.capitalize()}: ${price:.2f}\n")
        file.write("\n")
        total = processor.total_cost()
        file.write(f"Total Cost: ${total:.2f}\n")
    print(f"Order details have been saved to {filename}.")