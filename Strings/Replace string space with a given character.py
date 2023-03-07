string=input("Enter a string=")
char=input("Enter a character=")
result=''
for i in string:
    if i==' ':
        i=char
    result+=i
print("Result is",result)
