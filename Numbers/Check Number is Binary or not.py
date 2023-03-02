num=int(input("Enter a number="))
while num>0:
    rem=num%10
    if rem!=0 and rem!=1:
        print(" Number is not a binary number")
        break
    num=num//10
    if num==0:
        print("Number is a binary number")
