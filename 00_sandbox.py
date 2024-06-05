import pandas as pd

# lists to hold order into
pizza_order = ["cheese", "cheese", "shrimp"]
sides_order = ["pepsi"]
pizza_cost = [10, 10, 15]
sides_cost = [4]


# dict to organise order info
your_order_dict = {
    "Items": pizza_order + sides_order,
    "Price": pizza_cost + sides_cost
}

df = pd.DataFrame(your_order_dict)
print(df)
print("Your total is ${}".format((sum(sides_cost + pizza_cost))))

