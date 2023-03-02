val=int(input("Enter a value="))
fact=1
if val==0:
    print("Please enter valid input")
for i in range(1,val+1):
    fact=fact*i
print("Facorial of",val,"is",fact)