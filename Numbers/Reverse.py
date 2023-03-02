n=int(input("Enter a Number="))
result=0
while n!=0:
    rem=n % 10
    result=result * 10 + rem
    n=n//10
print("Reverse Number is",result)
