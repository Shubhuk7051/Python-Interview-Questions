def sum_of_digits(number):
    if number==0:
        return 0
    else:
        return((number%10) + sum_of_digits(int(number/10)))

num=int(input("Enter Number="))
print("Sum of digits in",num,"is",sum_of_digits(num))
