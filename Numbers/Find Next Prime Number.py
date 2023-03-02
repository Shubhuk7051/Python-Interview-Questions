def next_prime(num):
    x=num+1
    while True:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print("Next Prime is",x)
            break
        x+=1

number=int(input("Enter a number="))
next_prime(number)
    