
# Palindrome example
def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("radar"))
print(is_palindrome("radax"))



# almost palindrome example
# by deleting one chara it will be as palindrome

def is_almost_palindrome(string):
    for i in range(len(string)):
        current_string = string[:i]+string[i+1:]
        if current_string ==current_string[::-1]:
            return True
    return False


print(is_almost_palindrome("radkar"))
print(is_almost_palindrome("radario"))
