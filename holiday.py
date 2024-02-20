# ===== User-defined Functions - Practical Task 1 ===== #

# List of city destinations. Flight prices must be updated in plane_cost function.
cities = ['Paris', 'Cape Town', 'Palermo', 'Singapore']

# ========== Functions ==================================


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


def holiday_costs(hotel_cost, plane_cost, car_rental, num_nights, city_flight, rental_days):
    ''' Outputs cost breakdown and returns total holiday cost (float)'''
    hotel_total = hotel_cost(num_nights)
    car_total = car_rental(rental_days)
    plane_total = plane_cost(city_flight)
    print("----------------------------------------------\n"
          f"Cost breakdown for your holiday in {city_flight}:\n"
          f"Cost of Flight: £{plane_total:.2f}\n" +
          f"Total hotel cost ({num_nights} nights): £{hotel_total:.2f}\n"
          f"Car rental ({rental_days} days): £{car_total:.2f}\n"
          "----------------------------------------------")
    return hotel_total + car_total + plane_total


def get_valid_int(bounds=None):
    '''Gets user input and returns the input if it is an integer.
       Takes optional bounds argument to validate the range of the input.
    '''
    while True:
        try:
            user_input = int(input())
            # Check if the user has passed in a bounds argument.
            if bounds is not None:
                lower, upper = bounds
                if user_input >= lower and user_input <= upper:
                    return user_input
                else:
                    print("Out of range: Please enter a number from" +
                          f" {lower}-{upper}")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def menu(city_list):
    ''' Displays menu, collects user inputs and outputs holiday costs '''
    for index, city in enumerate(city_list, 1):
        print(index, ':', city)

    # Get data from user and call holiday_costs function to output cost breakdown and total cost.
    print("Please choose a destination (1-4) from the list below.")
    user_index = get_valid_int(bounds=(1, 4))
    city_flight = city_list[user_index - 1]
    print(f"How many nights would you like to stay in {city_flight}?")
    num_nights = get_valid_int()
    print("How many days would you like to hire a car for? (Enter 0 if you don't need a car)")
    rental_days = get_valid_int()
    print("The total cost of the holiday is: " +
          f"£{holiday_costs(hotel_cost, plane_cost, car_rental,
                            num_nights, city_flight, rental_days):.2f}" +
          "\n----------------------------------------------")


# Call menu function to start program if file is executed.
if __name__ == "__main__":
    menu(cities)
