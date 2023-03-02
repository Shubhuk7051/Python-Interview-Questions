num=int(input("Enter a Number="))
result=0
temp=num
while num!=0:
    rem=num%10
    result=result + rem**3
    num=num//10
if temp==result:
    print(temp,"is an Armstrong Number")
else:
    print(temp,"is not an Armstrong Number")
