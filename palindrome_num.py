n=int(input("Enter the number:"))
temp=n
rev=0
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if(rev==n):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
