# User to input how many students are registering
# Create a loop that runs for that number of students
# Each time the loop runs the program should ask the user to enter the next student ID number
# Write each of the ID numbers to a Text file called reg_form.txt
# Include a dotted line after each student ID number

number_of_students = int(input("How many students are registering? "))

with open("reg_form.txt", "w") as file:
    for i in range(number_of_students):
        student_id = input("Enter the next student ID number: ")
        file.write(student_id + "\n" + "\n")
        file.write("..." * 10 + "\n")