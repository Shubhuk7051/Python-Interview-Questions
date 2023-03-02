n=int(input("Enter a number="))

def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num%10) + str(reverse(num//10)))

def is_Palindrome(num):
    if num==reverse(num):
        return True
    return False
if is_Palindrome(n)==True:
    print(n,"is a Palindrome Number")
else:
    print(n,"is not a Palindrome Number")
