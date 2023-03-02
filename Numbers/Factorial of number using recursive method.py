def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

number=int(input("Enter a number="))
if number<0:
    print("Cannot be calulated")
elif number==0:
    print("Factorial of 0 is 1")
else:
    result=fact(number)
    print("Factorial of",number,"is",result)