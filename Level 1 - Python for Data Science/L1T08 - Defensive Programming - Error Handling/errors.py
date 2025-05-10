# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Added parenthesis {Syntax Error}
print("\n") # Added parenthesis and removed the space {Syntax Error}

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Removed "year's old" and changed == to = {Logical Error}
print("I'm " + str(age_Str) + " years old.") # Deleted the line that converted the age to an integer ; added str() to the age variable {Logical Error}

    # Variables declaring additional years and printing the total years of age
years_from_now = "3" # Declared 3 as a string {Runtime Error}
total_years = int(age_Str) + int(years_from_now) # Converted age_Str to an integer {Runtime Error}

print(total_years) 

    # Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old") # Added str() to the total_months {Runtime Error} ; added 6 months ; added parenthesis {Syntax Error}

#HINT, 330 months is the correct answer

