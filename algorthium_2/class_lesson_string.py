string = "this is the \"perfect\" example"
print(string)
print("This" in string)
string_1 = "one two three"
print("The string for the length", string[0:6])
print("Concating the 2 strings", string + " " + string_1)

for char in string_1:
    print("The each char is ", char)

print("The length of the string", len(string))
print("Lower case0", string.lower())
print("Upper case ", string_1.upper())
print("Split", string.split())
print("Split by t", string_1.split("t"))

list_word = ["apple", "orange", "Blueberry"]
new_word = "-".join(list_word)
print("The new join word is ", new_word)
print("Capitalise the word", new_word.capitalize())
string_3 = "   mouni    "
print(string_3)
print("Remove the space", string_3.strip())

fruit = "apple"
print("Replacing the letters", fruit.replace('p', 'P'))

print("Title ", string_1.title())
print("Find", string.find("i"))

str_format = "This is for formating 1:{}, 2:{} "
print(str_format.format(10,"one"))
