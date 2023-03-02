a=int(input("Enter First Number="))
b=int(input("Enter Second Number="))
c=int(input("Enter Third Number="))

if a>b and a>c:
    print(a,"is a greatest number")
elif b>a and b>c:
    print(b,"is a greatest number")
else:
    print(c,"is a greatest number")
