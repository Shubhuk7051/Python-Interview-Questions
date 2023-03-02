base=int(input("Enter base="))
power=int(input("Enter power="))
result=1
while power!=0:
    result=base * result
    power=-1
print(base,"to the power",power,"is",result)