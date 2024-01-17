# ========= 5: Capstone Project ========= #
import math

print(
"""
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
      
Enter either 'investment' or 'bond' from the menu above to proceed... 
""")

# Get input from user and assign to user_selection.
user_selection = input().lower()

# Investment Option.
if user_selection == 'investment':
    print("="*15, "Investment Calculator", "="*15)
    amount = float(input("How much money will you be depositing? ... "))
    rate = float(input("What is the interest rate (%) on the investment? ..."))
    time = int(input("What is the duration (in years) of the investment? ..."))
    interest = input("What type of interest do you want to calculate?\n"+ 
                      "Enter either 'simple' or 'compound' for the interest to be calculated ...").lower()
    
    if interest == 'simple':
        interest_paid =round(amount * (1 + (rate/100)*time), 2)
    elif interest == 'compound':
        interest_paid = round(amount * math.pow((1 + (rate/100)), time), 2)
        
    print("="*53)
    print(f"Interest paid: £{interest_paid}")

# Bond Option.
elif user_selection == 'bond':
    print("="*15, "Bond Calculator", "="*15)
    value = int(input("What is the present value of the house (£) ? ..."))
    rate = float(input("What is the interest rate (%) on the bond? ..."))
    time = int(input("How many month will it take to repay the bond? ..."))

    # Calculate monthly rate as decimal (i).
    i = rate/1200

    repayment = round((i * value)/(1 - (1+i)**(-time)), 2)

    print("="*47)
    print(f"You will pay £{repayment} per month.")