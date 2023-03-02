def prime_between_numbers(lowval,uppval):
    for num in range(lowval,uppval):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num,end=" ")

num1=int(input("Enter Lower Value="))
num2=int(input("Enter Upper Value="))
prime_between_numbers(num1,num2)