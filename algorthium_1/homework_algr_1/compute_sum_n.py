def sum_of_digits(n):
    total_sum = 0
    for i in range(1,n+1):
        while i>0:
            digit = i % 10
            total_sum = total_sum+digit
            i//=10
    print (f'The sum of digits in {n} is = {total_sum}')


sum_of_digits(5)