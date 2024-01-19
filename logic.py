# ===== Defensive Programming - Practical Task 2 ===== #

# Program to return n terms of Fibonacci sequence (1, 1, 2, 3, 5, 8, 13, 21 ...).

# Get the value of n from the user. Error handling to make sure an integer is assigned to n. 
while True:
    try: 
        n = int(input("Enter length of sequence, n= "))
        break
    except Exception as e:
        print("Please enter an integer value for n. The following error occurred:", e)

# LOGIC ERROR. With n=6, this incorrectly produces: 1, 1, 2, 3, 5, 8, 13, 21.
# The logic error results from the stop value in range.
# The original list (fib) already contains this first two terms in the sequence, meaning the final list will be the wrong length.
# It can be fixed by subtracting 2 from the stop value to account for two values already in the list.
fib = [1, 1]
for i in range(0, n): # <--- ERROR.
    u = fib[i] + fib[i+1]
    fib.append(u)
print(', '.join([str(x) for x in fib]))

# CORRECT VERSION. With n=6, this produces: 1, 1, 2, 3, 5, 8.
# A further improvement is to splice the final list using [:n].
# This would have the added benefit of producing the correct result if a user inputs n=1. 
fib = [1, 1]
for i in range(0, n-2):
    u = fib[i] + fib[i+1]
    fib.append(u)
print(', '.join([str(x) for x in fib[:n]]))
