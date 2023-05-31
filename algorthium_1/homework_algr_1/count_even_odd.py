def count_odd_even_digits(number):
    odd_count = 0
    even_count = 0
    number = abs(number)  # Convert negative numbers to positive

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number //= 10

    return odd_count, even_count


number = 34560
odd_digits, even_digits = count_odd_even_digits(number)
print("Number of odd digits:", odd_digits)
print("Number of even digits:", even_digits)
