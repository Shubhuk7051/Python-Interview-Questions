def decimaltobinary(num):
    if num>=1:
        decimaltobinary(num//2)
    print(num%2,end='')

    
number=int(input("Enter a number="))
decimaltobinary(number)