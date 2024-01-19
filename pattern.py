# ========= For Loops - Practical Task 1 ========= #

for row_num in range(1, 10):
    if row_num <= 5:
        print('*'*row_num)
    else:
        print('*'*(10 - row_num))