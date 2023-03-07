string=input("Enter a string=")
char_freq={}
for i in string:
    if i in char_freq:
        char_freq[i]+=1
    else:
        char_freq[i]=1
print("Highest Frequency character is",max(char_freq,key=char_freq.get))
