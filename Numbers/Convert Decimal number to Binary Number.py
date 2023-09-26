def decimaltobinary(num):
    if num>=1:
        decimaltobinary(num//2)
    print(num%2,end='')

    
number=int(input("Enter a number="))
decimaltobinary(number)

def decimaltobinary(n):

    assert int(n) == n, 'The number must be an integer"

    if n==0:
        return 0
    else:
        return n%2 + 10 * decimaltobinary(n//2)
