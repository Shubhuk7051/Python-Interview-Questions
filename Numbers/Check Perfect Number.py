def check_perfect(num):
    sum=0
    for i in range(1,int(num/2)+1):
        rem=num%i
        if rem==0:
            sum=sum+i
    if sum==num:
        print(num,"is a perfect number")
    else:
        print(num,"is not a perfect number")

number=int(input("Enter a number="))
result=check_perfect(number)
    