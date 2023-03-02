def lcm_of_numbers(num1,num2):
    LCM=max(num1,num2)
    while LCM <= num1*num2:
        if LCM%num1==0 and LCM%num2==0:
            print("LCM of",num1,"and",num2,"is",LCM)
            break
        LCM+=1

number1=int(input("Enter first number="))
number2=int(input("Enter second number="))
lcm_of_numbers(number1,number2)