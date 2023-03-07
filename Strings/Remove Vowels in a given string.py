string=input("Enter a number=")
result=''
for i in string:
    if i in 'aeiou' or i in 'AEIOU':
        i=' '
    result+=i
print("Result is=", result)
