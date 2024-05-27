# functions go here

# main routine goes here
while True:
    ordered_before = input("Have you ordered with us before?").lower()

    if ordered_before == "no" or ordered_before == "n":
        print("instructions go here")

    elif ordered_before == "yes" or ordered_before == "y":
        pass

    else:
        print("Please answer yes or no")
