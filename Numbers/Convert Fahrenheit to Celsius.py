def fah_to_cel(temp):
    result=((temp-32) * 5) / 9
    print(temp,"F is in Celsius is",result,"C")

temp=float(input("Enter temperature in Fahrenheit="))
fah_to_cel(temp)