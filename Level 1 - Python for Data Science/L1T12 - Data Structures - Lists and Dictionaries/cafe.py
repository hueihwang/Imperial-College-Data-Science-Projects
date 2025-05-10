# Create a list called "menu" tbat contains the following items: "Hokkien Mee", "Chicken Rice", "Bee Hoon Soup", "Mee Siam"
# Create a dictionary called "stock" that contains the stock vakue for each item in the menu. "Hokkien Mee" has 10, "Chicken Rice" has 20, "Bee Hoon Soup" has 30, "Mee Siam" has 40
# Create a dictionary called "price" that contains the price for each item in the menu. "Hokkien Mee" has 3.5, "Chicken Rice" has 4.0, "Bee Hoon Soup" has 3.0, "Mee Siam" has 3.5
# Loop through the menu and calculate the item's total value by multiplying the stock value with the price value
# Calculate the total value of all items in the menu

menu = ["Hokkien Mee", "Chicken Rice", "Bee Hoon Soup", "Mee Siam"]
stock = {
    "Hokkien Mee": 10, 
    "Chicken Rice": 20, 
    "Bee Hoon Soup": 30, 
    "Mee Siam": 40
}

price = {
    "Hokkien Mee": 18, 
    "Chicken Rice": 16, 
    "Bee Hoon Soup": 18.8, 
    "Mee Siam": 10
}

for item in menu:
    item_value = stock[item] * price[item]
    total_value = sum([stock[item] * price[item] for item in menu])
    print(f"The total value of {item} is ${item_value}")
    print(f"The total value of all items is ${total_value}")

