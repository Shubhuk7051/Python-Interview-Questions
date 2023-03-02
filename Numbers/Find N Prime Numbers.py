def prime_numbers(num):
    x=2
    while num:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x,end=" ")
            num-=1
        x+=1
    
n=int(input("Enter the number="))
prime_numbers(n)