# ========= IO Operations - Practical Task 1 ========= #

# Initialise empty lists for names and birthdates.
names = []
birthdates = []

# Open DOB.txt and convert each line to a list of the elements.
# Append first two elements to names list and remaining elements to birthdates.
with open ('./DOB.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line_list = line.strip().split(' ')
        names.append(line_list[:2])
        birthdates.append(line_list[2:])


# Output heading using ANSI escape code for bold console text (\033[1m).
print("\033[1mName \033[0m")

# Output list of names on a new line after joining the list. 
for name in names:
    print(' '.join(name))

# Repeat the same process birthdates list. \n  included to separate the sections.
print("\n\033[1mBirthdate \033[0m")
for date in birthdates:
    print(' '.join(date))