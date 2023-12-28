### While Loops ######
### Practical Task 1 #
######################

sum = 0
count = 0
user_input= float(input("Please enter a number or enter -1 to exit"))
while user_input != -1:
    sum += user_input
    count += 1
    user_input = float(input("Please enter a number or enter -1 to exit"))
 
print(f"The average of the numbers is: {round(sum/count, 2)}")
