def validation():
    while True:
        user_input = input("Enter a number: ")
        try:
            output = float(user_input)
            if output > 0:
                return output
        except ValueError:
            print("Enter a valid number greater than 0")

number = validation()