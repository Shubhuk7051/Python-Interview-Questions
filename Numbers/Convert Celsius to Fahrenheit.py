def cel_to_fah(temp):
    result=(9/5 * temp) + 32
    print(temp,"C is in Fahrenheit is",result,"F")
    
temp=float(input("Enter temperature in celsius="))
cel_to_fah(temp)