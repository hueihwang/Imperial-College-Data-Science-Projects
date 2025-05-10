# User to input full name
# If blank, print "You haven't entered anything. Please enter your full name."
# If entered less than 4 characters, print "You have entered less than 4 characters. Please make sure that you have entered your name and surname."
# If entered more than 25 characters, print "You have entered more than 25 characters. Please make sure that you have only entered your full name."
# If entered between 4 and 25 characters, print "Thank you for entering your name."

name = input("Please enter your full name: ")
if name == "":
    print("You haven't entered anything. Please enter your full name.")
elif len(name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")