# === String Handling - Practical Task 1 === #

# Get a string from the user.
user_string = input("Please enter any string. ")

# Create empty string.
alternating_letters = ''
# Iteration to form alternating upper/lower characters and append to alternating_letters.
for index, char in enumerate(user_string):
    if index % 2 == 0:
        alternating_letters += char.upper()
    else:
        alternating_letters += char.lower()

# Test output.
print(alternating_letters)
    
# Split string into list of words, using a single space as separator. 
word_list = user_string.split(' ')

# Iteration to make alternating words in list upper then lower.
for index, word in enumerate(word_list):
    if index % 2 == 0:
        word_list[index] = word.upper()
    else:
        word_list[index] = word.lower()

# Create string by joining word_list with a single space separator.
alternating_words = ' '.join(word_list)

# Test output.
print(alternating_words)
