# User to input triathlon time in minutes
    # Swiming time
    # Cycling time
    # Running time

# Calculate the total time in minutes

# If total time is in between 0 and 100 minutes, print "Award: Provincial Colours"
# If total time is in between 101 and 105 minutes, print "Award: Provincial Half Colours"
# If total time is in between 106 and 110 minutes, print "Award: Provincial Scroll"
# If total time is in above 111 minutes, print "No Award"

swimming_time = int(input("Enter swimming time in minutes: "))
cycling_time = int(input("Enter cycling time in minutes: "))
running_time = int(input("Enter running time in minutes: "))
total_time = swimming_time + cycling_time + running_time
print("Total time:", total_time, "mins")

if total_time <= 100:
    print("Award: Provincial Colours")
elif total_time <= 105 and total_time >= 101:
    print("Award: Provincial Half Colours")
elif total_time <= 110 and total_time >= 106:
    print("Award: Provincial Scroll")
else:
    print("No Award")