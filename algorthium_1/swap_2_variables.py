a = 5
b = 10

print(f'Before swaping  a={a} and b={b}')

# O(1) for all 3 solutions

# First solution
# temp = a
# a = b
# b = temp

# second solution
# a, b = b, a

# Third solution: (For chara for a and b  it wont work)
a = a + b
b = a - b
a = a - b

print(f'After swaping a={a} and b={b}')
