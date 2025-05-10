# Request user to enter 3 seperate numbers(integers)
# Print the sum of the 3 numbers
# Print the first number minus the second number
# Print the third number multiplied by the first number
# Print the sum of all three numbers divided by the third number

input1 = int(input("Enter the first number: "))
input2 = int(input("Enter the second number: "))
input3 = int(input("Enter the third number: "))

print("The sum of the three numbers is: ", input1 + input2 + input3)
print("The first number minus the second number is: ", input1 - input2)
print("The third number multiplied by the first number is: ", input3 * input1)
print("The sum of all three numbers divided by the third number is: ", (input1 + input2 + input3) / input3)