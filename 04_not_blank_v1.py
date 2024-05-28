# functions go here
# checks that the response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Please try again, your response cannot be blank.")
        else:
            return response


# main routine here
while True:
    name = not_blank("Enter your name (or xxx to quit)")

    if name == "xxx":
        break

print("Your name is {}".format(name))
print("Done")
