# ===== Practical Task 1 ===== #

# Get input from user, cast to integer and assign to variables
swim_time = int(input("Enter the swimming time (mins)... "))
cycle_time = int(input("Enter the cycling time (mins)... "))
run_time = int(input("Enter the running time (mins)... "))

# Calculate total time and assign to total_time
total_time = swim_time + cycle_time + run_time

# Control statement to determine qualifying criteria
if total_time <= 100:
    award = "Provincial Colours"
elif total_time >= 101 and total_time <= 105:
    award = "Provincial Half Colours"
elif total_time >= 106 and total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

# Output total time and award
print('='*40)
print(f"Total triathlon time is: {total_time} minutes.\nThe award is: {award}.")
print('='*40)


