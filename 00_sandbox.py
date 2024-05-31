reg_menu = ["cheese", "pepperoni", "hawaiian", "meatball", "vegetarian"]
reg_price = [10, 12, 12, 15, 15]

pizza_order = []
sides_order = []

order_dict = {
    "Pizza": pizza_order,
    "Sides": sides_order
}

# goal - start off with a set order and using the lists calculate the price
# then move to making it work for any order


chosen_pizza = "meatball"
chosen_sides = "mozzarella sticks"

pizza_order.append(chosen_pizza)
sides_order.append(chosen_sides)

val = reg_menu.index(chosen_pizza)
for i, val in enumerate(reg_price):
    price = reg_price[i]
print(pizza_order, price)


