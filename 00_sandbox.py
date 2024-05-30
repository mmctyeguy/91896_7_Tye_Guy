def hello():
    hello.counter += 1
    return hello.counter


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes/no")


hello.counter = 0

while True:
    calling = yes_no("question?")
    if calling == "yes":
        hello()
        print(hello.counter)
