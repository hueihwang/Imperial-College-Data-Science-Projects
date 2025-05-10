# User to input a sentence
# Save the user's response in a variable called "str_manip"
# Calculate and dsiplay the length of str_manip
# Find the last letter in str_manip.
    # Replace all of the specific letter with a new letter "@".
# Print the last 3 characters in str_manip backwards.
# Create a 5-letter word that is made up of the first 3 characters and the last 2 characters of str_manip.

str_manip = input("Enter Sentence: ")
str_manip_no_space = str_manip.replace(" ", "")
print(len(str_manip_no_space))

last_letter = str_manip[-1:]
replace_sentence = str_manip.replace(last_letter, "@")
print(replace_sentence)

last_three_letters_backwards = str_manip[:-4:-1]
print(last_three_letters_backwards)

new_word = str_manip[:4] + str_manip[-2:]
print(new_word)