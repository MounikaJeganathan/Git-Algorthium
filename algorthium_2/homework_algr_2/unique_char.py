def has_unique_characters(string):
    seen_characters = set()

    for char in string:
        if char in seen_characters:
            return False
        seen_characters.add(char)

    return True


string1 = 'abcde'
print(has_unique_characters(string1))  # Output: True

string2 = 'aabcde'
print(has_unique_characters(string2))  # Output: False


def unique_char(s):
    length_str = len(s)
    length_set = len(set(s))
    return length_set == length_str


print(unique_char('abcd'))
print(unique_char('aabbcd'))
