# === Data Structures - Practical Task === #

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
    "Americano" : 4.00,
    "Tea" : 2.00,
    "Orange Juice" : 4.80
    }

# Loop to calculate total stock value.
total_stock = 0
for item in menu:
    total_stock += price[item] * stock[item]

print(f"The total value of the stock is: £{total_stock}")
    