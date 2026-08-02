n=int(input("Enter the number:"))
temp=n
s=0
while(temp>0):
    digit=temp%10
    s=s+digit**3
    temp=temp//10
if(s==n):
    print("It is a Armstrong number")
else:
    print("It is not a Armstrong number")
