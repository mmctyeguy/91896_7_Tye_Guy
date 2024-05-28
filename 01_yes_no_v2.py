def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


# main routine goes here
while True:
    ordered_before = yes_no("do you want to read the instructions?")

    if ordered_before == "no":
        print("instructions go here")

    print("program continues...")
    print()
