# ===== User-defined Functions - Practical Task 1 ===== #

# List of city destinations. Flight prices must be updated in plane_cost function.
cities = ['Paris', 'Cape Town', 'Palermo', 'Singapore']

# ===== Function declarations =======


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
    ''' Outputs cost breakdown and returns total holiday cost (float)'''
    hotel_total = hotel(num_nights)
    car_total = car(rental_days)
    plane_total = plane(city_flight)
    print("----------------------------------------------\n"
          f"Cost breakdown for your holiday in {city_flight}:\n"
          f"Cost of Flight: £{plane_total}\n"
          f"Total hotel cost ({num_nights} nights): £{hotel_total}\n"
          f"Car rental ({rental_days} days): £{car_total}\n"
          "----------------------------------------------")
    return hotel_total + car_total + plane_total


def get_valid_int(bounds=None):
    '''Gets user input and returns user_input if it is an integer.
       Takes optional bounds argument to validate the range of the input.
    '''
    while True:
        try:
            user_input = int(input())
            if bounds is not None:
                lower, upper = bounds
                if user_input >= lower and user_input <= upper:
                    return user_input
                else:
                    print(f"Out of range: Please enter a number from 
                          {lower}-{upper}")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def menu(city_list):
    ''' Displays menu, collects user inputs and outputs holiday costs '''
    for index, city in enumerate(city_list, 1):
        print(index, ':', city)

    print("Please choose a destination from the list below.")
    user_index = get_valid_int(bounds=(1, 4))
    city_flight = city_list[user_index - 1]
    print(f"How many nights would you like to stay in {city_flight}?")
    num_nights = get_valid_int()
    print("How many days would you like to hire a car for? (Enter 0 if you don't need a car)")
    rental_days = get_valid_int()
    print("The total cost of the holiday is: £",
          holiday_costs(hotel_cost, plane_cost, car_rental,
                        num_nights, rental_days, city_flight),
          "\n----------------------------------------------")


# Call menu function to start program.
menu(cities)
