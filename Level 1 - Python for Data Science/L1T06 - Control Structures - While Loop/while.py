# User to input a number
# Python to ask the user to continue inputting numbers until the user inputs "-1"
# Once the user inputs "-1", the loop will break
# The program will calculate the average all the numbers inputted by the user
# The program will print the average of all the numbers

total_value = 0
num_of_integers = 0

user_input = int(input("Enter a number (Enter -1 to exit): "))

while user_input != -1:
    total_value += user_input
    num_of_integers += 1
    user_input = int(input("Enter a number (Enter -1 to exit): "))
   
    if user_input == -1:
        break

average = total_value / num_of_integers
print("Average: ", average)


