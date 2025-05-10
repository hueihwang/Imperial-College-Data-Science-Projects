# User to input "city_flight", "num_nights" and "rental_days" 
# Create function "hotel_cost()" which takes "num_nights“ as argument and return a total cost for the hotel stay
# Create function "plane_cost()" which takes city_flight as argument and return a total cost for the flight
# Use if/else statement in the function to retrieve a price based on the chosen city
# Create function "car_rental()" which takes "rental_days" as argument and return a total cost for the car rental
# Create function "holiday_cost()" which takes "city_flight", "num_nights" and "rental_days" as arguments
# Using these three arguments, call the "hotel_cost()", "plane_cost()" and "car_rental()" functions and return the total cost of the holiday
# Print each of the costs and the total cost of the holiday

print("List of available cities to fly to: Penang, Kuala Lumpur, Johor Bahru")

valid_cities = ["penang", "kuala lumpur", "johor bahru"]
while True:
    city_flight = input("Please select the city you are flying to: ").strip().lower()
    if city_flight in valid_cities:
        break
    else:
        print("Invalid city, please select from the list of available cities")


while True:
    try:
        num_nights = int(input("Please enter the number of nights you are staying: "))
        if num_nights > 0:
            break
        else:
            print("Please enter a valid number of nights")
    except ValueError:
        print("Please enter a valid number of nights")

while True:
    try:
        rental_days = int(input("Please enter the number of days you are renting a car: "))
        if rental_days > 0:
            break
        else:
            print("Please enter a valid number of days")
    except ValueError:
        print("Please enter a valid number of days")

def hotel_cost(num_nights):
    hotel_price_per_night = 200
    return num_nights * hotel_price_per_night

def plane_cost(city_flight):
    if city_flight == "penang":
        return 250
    elif city_flight == "kuala lumpur":
        return 700
    elif city_flight == "johor bahru":
        return 500
    else:
        return 0
    
def car_rental(rental_days):
    car_price_per_day = 100
    return rental_days * car_price_per_day

def holiday_cost(city_flight, num_nights, rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

print("The total cost of the hotel stay is: RM", hotel_cost(num_nights))
print("The total cost of the flight is: RM", plane_cost(city_flight))
print("The total cost of the car rental is: RM", car_rental(rental_days))
print("The total cost is: RM", holiday_cost(city_flight, num_nights, rental_days))