string=input("Enter a string=")
alpha=''
others=''
for i in string:
    if i.isalpha():
        alpha+=i
    else:
        others+=i
print("Separate Alphabets=",alpha)
print("Separate other characters=",others)
