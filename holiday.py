# ===== User-defined Functions - Practical Task 1 ===== #

# Function declarations.
def hotel_cost (num_nights):
    hotel_price = 105.00
    return hotel_price * num_nights

def plane_cost (city_flight):
    city_prices = {
          'Paris' : 89.00,
          'Cape Town': 760.00,
          'Palermo' : 120.00,
          'Singapore': 990.00
          }
    return city_prices[city_flight]

def car_rental(rental_days):
    rental_price = 35.00
    return rental_price * rental_days

def holiday_costs(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)


cities =[ 'Paris', 'Cape Town', 'Palermo', 'Singapore']
print ("Please choose a destination from the list below.")
for index, city in enumerate(cities, 1):
    print(index, ':', city)

user_input = input().lower()
if user_input ==1 or cities[0]:
    city_flight = 'Paris'
elif user_input ==2 or 'cape town':
    city_flight = 'Cape Town'
else:
    print("Not a valid option.")

num_nights = int(input(f"How many nights would you like to stay in {city_flight}?"))
rental_days = int(input("How many days would you to hire a car for? (Enter 0 if you don't need a car)"))

print(f"The total cost of the holiday is: £{holiday_costs()}")