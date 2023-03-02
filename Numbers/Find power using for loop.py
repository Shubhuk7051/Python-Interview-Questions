base=int(input("Enter base="))
power=int(input("Enter power="))
result=1
for i in range(power):
    result*=base
print(base,"to the power",power,"is",result)