a,b=0,1
n=int(input("Enter a Value:"))
def fibo_series(num):
    if num==0:
        return a
    elif num==1:
        return b
    else:
        return (fibo_series(num-1) + fibo_series(num-2))

print("Fibonacci Series are:")
for i in range(0,n):
    print(fibo_series(i))
