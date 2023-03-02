def hcf_of_numbers(num1,num2):
    HCF=min(num1,num2)
    while  HCF:
        if num1%HCF==0 and num2%HCF==0:
            print("HCF of",num1,"and",num2,"is",HCF)
            break
        HCF-=1

number1=int(input("Enter first number="))
number2=int(input("Enter second number="))
hcf_of_numbers(number1,number2)