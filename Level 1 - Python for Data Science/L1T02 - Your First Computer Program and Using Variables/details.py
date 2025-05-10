#input: User's Name, Age, House Number, Street Name
#Print: This is (User's Name). He is (Age) years old and lives at house number (House Number) on (Street Name).

name = str(input("User's Name: "))
age = int(input("Age: "))
house_number = int(input("House Number: "))
street_name = str(input("Street Name: "))

print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")