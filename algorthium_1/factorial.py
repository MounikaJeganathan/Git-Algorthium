# O(n) solution
n = 5
result = 1

while n > 0:
    print(f'n={n} and result = {result}')
    result = result * n
    n = n - 1

print(f'The factorial of {n} is = {result}')
