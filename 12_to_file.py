import pandas
import random
from datetime import date

# lists to hold ticket details
pizza_order = ["cheese", "shrimp"]
sides_order = ["pepsi", "garlic bread"]
pizza_cost = [10.00, 12.00]
sides_cost = [3.99, 12.00]
extra_cost = [1.5]
extra_reason = ["delivery charge"]

your_order_dict = {
    "Items": pizza_order + sides_order + extra_reason,
    "Price": pizza_cost + sides_cost + extra_cost
}

your_order_frame = pandas.DataFrame(your_order_dict)

# **** get current date for heading and filename ****
# get today's date
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")


heading = "---- Pizza Order({}/{}/{}) ----\n".format(day, month, year)
filename = "PIZZA_{}_{}_{}".format(year, month, day)

# change frame to a string, so we can export it to a file
your_order_string = pandas.DataFrame.to_string(your_order_frame)

# list holding content to print/write to file
to_write = [heading, your_order_string]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
