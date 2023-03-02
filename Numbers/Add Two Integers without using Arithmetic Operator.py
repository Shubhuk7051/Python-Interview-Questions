def add_integers(a,b):
    for i in range(1,b+1):
        a=a+1
    return a

num1=int(input("Enter first number="))
num2=int(input("Enter second number="))
result=add_integers(num1,num2)
print("Sum of two integers=",result)