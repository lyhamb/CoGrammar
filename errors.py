# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # <--- SYNTAX ERROR. Added brackets to print functions. 
print ("\n")                           # <--- SYNTAX ERROR. Removed indent from this line and following lines. 

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # <--- RUNTIME ERROR (NameError). == operator used (equality) used instead of = operator (assignment).
age = int(age_Str) # <--- RUNTIME ERROR (Type). Can't cast an alphanumeric string to int. Removed 'years old' from age_Str variable. 
print("I'm " + age_Str + " years old.") # <--- RUNTIME ERROR (Type). Not possible to concatenate int and string. Changed variable to age_Str. Added spaces.

years_from_now = "3"
total_years = age + int(years_from_now) # <--- RUNTIME ERROR (Type). Can't perform add operation on a string value. Cast to int first. 

print ("The total number of years: " + str(total_years)) # <--- LOGIC ERROR. Author intended to use a variable here but instead used the string "answer_years".
                                                         #                   Changed to total_years variable which is cast to string. 

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # <--- RUNTIME ERROR (NameError). The total variable has not been defined. Author intended to use total_years.
print ("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old") # <--- SYNTAX ERROR. Added brackets to print function. 
                                                                                    #      RUNTIME ERROR (Type). Can't concatenate int and string. 
                                                                                    #      Cast total_months to string. 
                                                                                    #      LOGIC ERROR. Need to add 6 to total to account for extra 6 months. 

#HINT, 330 months is the correct answer

