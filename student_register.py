# ======= IO Output - Practical Task 1 ======= #

# Output file name set here:
file_name ="reg_form.txt"

# Get number of students from user and store as num_of_students.
while True:
    try:
        num_of_students = int(input("How many students will be registering? "))
        break
    except ValueError:
        print("Error: Please enter a whole number.")

student_list = []
# For loop to get student ID and append to student_list. IDs must consist of 5 numbers.
for i in range(0, num_of_students):
    while True:
        student_id = input("Please enter student ID: ")
        if len(student_id) == 5 and student_id.isnumeric():
            print(f"Thank you, student {i+1} registered")
            student_list.append(student_id)
            break
        else:
            print("This is a required field. Please enter a 5 digit number.")

# Open file (create file if it doesn't exist). Write student_list to file with dotted line.
try:
    with open(file_name, 'w+') as file:
        file.write("Exam Attendance Register.\n\nID     Sign here\n\n")
        for id in student_list:
            file.write(id + ': ' + '.'*25 + '\n\n')
except Exception as e:
    print("An error occurred whilst writing to the file:", e)
else: 
    print(f"Attendance registered created as: {file_name}")
finally:
    print("Exiting...")