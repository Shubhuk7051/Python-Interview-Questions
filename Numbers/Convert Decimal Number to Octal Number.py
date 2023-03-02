def decimaltooctal(num):
    if num>=1:
        decimaltooctal(num//8)
    print(num%8,end='')

    
number=int(input("Enter a number="))
decimaltooctal(number)