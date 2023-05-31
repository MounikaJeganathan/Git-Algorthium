# A leap is exactly div by 4 if its not ending with 00
# for century yr it is perfectly div by 400

# O(1)
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is the leap year')
            else:
                print(f'{year} is NOT an leap year')
        else:
            print(f'{year} is the leap year')
    else:
        print(f'{year} is  NOT the leap year')

leap_year(2000)
leap_year(1900)
leap_year(1975)
leap_year(2016)

