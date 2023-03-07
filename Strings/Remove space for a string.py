string=input("Enter a string=")
for i in range(len(string)):
    if string[i]==' ':
        string=string[:i] + string[i+1:]
        break
print("After remove space from string=",string)
