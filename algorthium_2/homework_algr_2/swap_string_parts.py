# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


# o(1)
def swap_parts_string(s):
    length = len(s)   # 11
    half_length = length // 2 #5
    if length % 2 == 1:
        half_length = half_length + 1  #6

    first_part = s[:half_length]
    second_part = s[half_length:]

    swapped_string = second_part + first_part
    return swapped_string


print(swap_parts_string("bbbbbcaaaaa"))
print(swap_parts_string('aaaabbbb'))