# Save "The!quick!brown!fox!jumps!over!the!lazy!dog." as a string.

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence)

new_sentence = sentence.replace("!"," ")
print(new_sentence)

upper_new_sentence = new_sentence.upper()
print(upper_new_sentence)

reversed_upper_new_sentence = upper_new_sentence[::-1]
print(reversed_upper_new_sentence)