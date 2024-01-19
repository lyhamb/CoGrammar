# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # <--- RUNTIME ERROR (NameError). Python thinks Lion is a variable that is not defined. 
                #                                 Lion is intended as a string and therefore should be inside "".
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # <--- LOGIC ERROR. Sentence won't make sense.
                                                                                            #      number_of_teeth and animal_type are the wrong way around. 
                                                                                            #      SYNTAX ERROR. Variables will not be inserted.
                                                                                            #      Changed to an f-string. 

print (full_spec) # <--- SYNTAX ERROR. Print function needs brackets enclosing the string. 

