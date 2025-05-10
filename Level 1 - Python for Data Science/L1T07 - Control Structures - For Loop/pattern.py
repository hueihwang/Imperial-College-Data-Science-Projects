# Use single for loop to print the star pattern from one start to five stars
# Reverse the pattern from five stars to one star using if statement

for i in range(1, 6):
    print('*' * i)
    if i == 5:
        for x in range(4, 0, -1):
            print('*' * x)