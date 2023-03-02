def check_palindrome(num):
    result=0
    temp=num
    while num!=0:
        rem=num%10
        result=result *10 + rem
        num=num//10
    return result

n=int(input("Enter a number:"))
answer=check_palindrome(n)
if n==answer:
    print(n,"is Palindrome Number")
else:
    print(n,"is not Palindrome Number")
