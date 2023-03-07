string=input("Enter a string=")
alpha,digit,special_char=0,0,0
for i in string:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
    else:
        special_char+=1
print("Count of alphabets is",alpha,",digits is",digit,"and special character is",special_char,"in given string.")
