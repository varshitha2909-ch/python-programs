x1=int(input("Enter number of terms:"))
a=0
b=1
for i in range(x1):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
