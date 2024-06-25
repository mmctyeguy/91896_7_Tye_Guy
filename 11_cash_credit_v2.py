def payment_type():
    payment_method = input("please select your payment method. Cash or credit? (ca/cr)")
    if payment_method == "cash" or payment_method == "ca":
        print("You have selected cash as your payment type")
        return "cash"
    elif payment_method == "credit" or payment_method == "cr":
        print("You have selected credit as your payment type.\n"
              " Please be aware that there is a 15% surcharge for credit.")
        return "credit"


