string=input("Enter a string=")
dup_chr=[]
for i in string:
    if i not in dup_chr:
        dup_chr.append(i)
for ele in range(0,len(dup_chr)):
    print(dup_chr[ele],end='')
    
