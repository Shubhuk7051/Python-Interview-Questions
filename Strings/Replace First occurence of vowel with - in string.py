string=input("Enter a string=")
ch='a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U'
for i in range(len(string)):
    if string[i]==ch:
        string=string[:i] + string[i+1:]
        break
print("Result is:",string)
