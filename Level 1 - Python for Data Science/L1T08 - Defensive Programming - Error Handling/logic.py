# Create Syntax, Logical and Runtime Error examples

# Syntax Error
# Huei trying to bake a bread

for baking_ingredients in ["flour", "sugar", "salt", "yeast"] #Missing ":" at the end
    print(f"Adding {baking_ingredients} to the bowl.")

# Runtime Error
# Huei trying to calculate the brew time of a cup coffee

water_temp = 80 # the temperature of the water in Celcius
coffee_weight = 0 # in grams

time = temp / coffee_weight #Divide by zero error
print(f"The brew time is {time} minutes.")

# Logical Error
# Huei trying to calculate the total price of a meal

meal_price = 10 # the price of the meal in dollars
tip = 0.15 # the tip percentage
tax = 0.07 # the tax percentage

total_price = meal_price + meal_price * tip * tax #Wrong calculation
print(f"The total price of the meal is {total_price} dollars.")