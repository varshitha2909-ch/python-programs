num=int(input("Enter any number:"))
c=0
for x in range(1,num+1):
    if(num%x==0):
        c+=1
if(c==2):
    print(num,": It is prime number")
else:
    print(num,": It is not a prime number")
