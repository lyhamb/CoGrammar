# ======== Data Structures - Practical Task ======== #

# Create menu list with four cafe items.
menu = ["Espresso", "Americano", "Tea", "Orange Juice"]

# Create dictionary with stock values per item.
stock = {
    "Espresso" : 40,
    "Americano" : 50,
    "Tea" : 100,
    "Orange Juice" : 20
    }

# Create dictionary with price (£) per item.
price = {
    "Espresso" : 3.50,
    "Americano" : 4.35,
    "Tea" : 2.00,
    "Orange Juice" : 4.80
    }

# For loop to calculate total stock value.
total_stock = 0
for item in menu:
    total_stock += price[item] * stock[item]

# Format to ensure 2 decimal places for currency (e.g. 230.5 would become 230.50).
# Rounding to 2 d.p in case any non-integers are used for stock values. 
total_stock_currency = '{:.2f}'.format(round(total_stock, 2))

# Output result
print(f"The total value of stock is: £{total_stock_currency}")  