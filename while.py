# ========= While Loops - Practical Task 1 ========= #

# I thought of two ways of doing this, I'm not sure which is the best!

# Implementation 1

sum = 0
count = 0
user_input= float(input("Please enter your first number ... "))
while user_input != -1:
    sum += user_input
    count += 1
    user_input = float(input("Please enter the next number (-1 to exit) ... "))
 
print(f"The average of the numbers is: {round(sum/count, 2)}")

# Implementation 2

sum = 0
count = 0
while True:
    user_input = float(input("Please enter the a number (-1 to exit) ... "))
    if user_input == -1:
        break
    sum += user_input
    count += 1
    
print(f"The average of the numbers is: {round(sum/count, 2)}")