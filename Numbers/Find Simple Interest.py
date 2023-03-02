def simple_interest(p,r,t):
    si=(p * r * t)/100
    print("Simple Interest is",si)
    
p=eval(input("Enter Principal Amount="))
r=eval(input("Enter rate of interest="))
t=eval(input("Enter time period="))
simple_interest(p,r,t)
