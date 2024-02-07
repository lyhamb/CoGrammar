# ===== User-defined Functions - Practical Task 1 ===== #

# List of city destinations. Flight prices must be updated in plane_cost function.
cities = ['Paris', 'Cape Town', 'Palermo', 'Singapore']

# Function declarations.


def hotel_cost(num_nights):
    ''' Takes number of nights (int) returns total hotel cost (float)'''
    hotel_price = 105.00
    return hotel_price * num_nights


def plane_cost(city_flight):
    ''' Takes destination city (string) as argument returns the flight cost (float)'''
    if city_flight == "Paris":
        return 89.00
    elif city_flight == "Cape Town":
        return 760.00
    elif city_flight == "Palermo":
        return 120.00
    elif city_flight == "Singapore":
        return 1240.00
    else:
        print("City not found.")
        

def car_rental(rental_days):
    '''Takes number of days (int) returns total rental price (float)'''
    rental_price = 35.00
    return rental_price * rental_days


def holiday_costs(hotel, plane, car, num_nights, rental_days, city_flight):
    ''' Outputs cost breakdown and returns total holiday cost as float'''
    hotel_total = hotel(num_nights)
    car_total = plane(rental_days)
    plane_total = car(city_flight)
    print("------------------------------------\n" +
          f"Cost breakdown for your holiday in {city_flight}\n" +
          f"Total hotel cost: £{hotel_total}\n"
          f"Car rental: £{car_total}\n" +
          "---------------------------------------")
    return hotel_total + car_total + plane_total


def menu(city_list):
    ''' Displays menu, collects user inputs and returns holiday_costs '''
    for index, city in enumerate(city_list, 1):
        print(index, ':', city)
    print("Please choose a destination from the list below.")
    while True:
        user_index = int(input())
        break
    city_flight = city_list[user_index - 1]
    num_nights = int(
        input(f"How many nights would you like to stay in {city_flight}?"))
    rental_days = int(input("How many days would you to hire a car for?" +
                            "(Enter 0 if you don't need a car"))

    print(f"The total cost of the holiday is: £{
        holiday_costs(hotel_cost, plane_cost, car_rental, num_nights, rental_days, city_flight)}")

# Call menu function to start program.
menu(cities)
