# functions
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine here

get_int = num_check("How many do you want to order?",
                    " Please enter an integer more "
                    "than 0\n", int)

print("You have ordered {} pizzas".format(get_int))

