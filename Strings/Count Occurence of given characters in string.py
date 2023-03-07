string=input("Enter a String:")
char=input("Enter a character:")
count=0
for i in range(len(string)):
    if string[i]==char:
        count+=1
print("Count Occurence of given characters in string:",count)
