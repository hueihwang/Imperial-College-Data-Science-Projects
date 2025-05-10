# Make every even character in a string uppercase

string = "I am learning data science and it is hard"

final_string_1 = ""

for i in range(len(string)):
    if i % 2 == 0:
        final_string_1 += string[i].upper()
    else:
        final_string_1 += string[i].lower()

print(final_string_1)

''''''
# Split the sentence into individual characters
# Make every even word uppercase

final_string_2 = ""

words = string.split()

for i in range(len(words)):
    if i % 2 == 0:
        final_string_2 += words[i].upper() + " "
    else:
        final_string_2 += words[i].lower() + " "

print(final_string_2.strip())