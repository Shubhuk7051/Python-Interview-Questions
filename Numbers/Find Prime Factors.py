num=315
var=2
while (num>1):
    if (num%var==0):
        print(var,end=" ")
        num=num/10
    else:
        var+=1
