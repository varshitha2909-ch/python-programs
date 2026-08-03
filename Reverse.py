#Reverse a string
Data1=input("Enter the data:")
print(Data1[::-1])

#Reverse a number
Data2=int(input("Enter the number:"))
temp=Data2
rev=0
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print(rev) 
