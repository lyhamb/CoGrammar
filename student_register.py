# ======= IO Output - Practical Task 1 ======= #

while True:
    try:
        num_of_students = int(input("How many students will be registering? "))
        break
    except Exception as e:
        print("ERROR. Please enter a whole number", e)

student_list = []
for n  in range(0, num_of_students):
    while True:
        student_id = input("Please enter student ID number: ")
        if len(student_id) == 5:
            print("Thank you, student ID registered")
            break
        else:
            print("This is a required field. Please enter a 5 digit number.")
    
    student_list.append(student_id)

with open('reg_form.txt', 'w+') as file:
    file.write("Exam Register\n\n")
    file.write("ID     Sign here\n\n")
    for id in student_list:
        file.write(id + ': ' + '.'*25 + '\n\n')