def leap_year(year):
    if (year % 4==0 or year % 400==0):
        print(year,"is a Leap Year")
    else:
        print(year,"is not a Leap Year")

year=int(input("Enter Year="))
leap_year(year)