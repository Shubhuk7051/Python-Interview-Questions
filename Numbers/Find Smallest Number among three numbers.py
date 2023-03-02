def smallest_number(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        print(num1,"is a smallest number")
    elif num2 < num1 and num2 < num3:
        print(num2,"is a smallest number")
    else:
        print(num3,"is a smallest number")
        
n1=int(input("Enter first number="))
n2=int(input("Enter second number="))
n3=int(input("Enter third number="))
smallest_number(n1,n2,n3)