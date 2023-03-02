num=int(input("Enter a Number="))
a,b=0,1
if num < 0:
    print("Invalid Input. Please Input in Positive")
else:
    print("Fibonacci Series:")
    for i in range(0,num):
        if i<=1:
            c=i
        else:
            c=a+b
            a=b
            b=c
        print(c,end=' ')
    
