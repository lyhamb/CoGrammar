### Practical Task One ###

# Get input, cast to integer and asign it to age variable
age = int(input("Enter your age... "))

# Control structures to determine age and print response
if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >=  40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")