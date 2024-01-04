# Write a program that forms a list of first character of every word in another list
word_list = ["apple", "banana", "cherry", "date",""]
print("The list of words :",word_list)
first_chars = []

for word in word_list:
    if len(word) > 0:
        first_chars.append(word[0])
    else:
        print("Skipping empty word.")
print("List of first characters:", first_chars)