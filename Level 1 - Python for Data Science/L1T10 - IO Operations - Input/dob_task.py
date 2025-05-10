# Open DOB.txt and read the contents

# Split the lines into two lists, one for names and one for birthdates

# Print the names and birthdates


file = open('DOB.txt', 'r')
lines = file.readlines()
file.close()

names = []
birthdates = []

with open('DOB.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    name_parts = line.rsplit(maxsplit=3)
    name = ' '.join(name_parts[:-3])
    birthdate = ' '.join(name_parts[-3:])
    names.append(name)
    birthdates.append(birthdate)

print("Name")
for name in names:
    print(name)

print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)