size=int(input("Enter the size of an list="))
list1=[]

for i in range(0,size):
    elem=int(input("Enter the value on index "+str(i)+"= "))
    list1.append(elem)

avg=sum(list1)/size
print("Average of Numbers is",avg)