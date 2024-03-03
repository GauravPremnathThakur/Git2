num=int(input("Enter the number: "))

flag=1

if(num>1):
    for i in range(2,num):
        if(num%i==0):
            flag=0
        
else:

if(flag==1):
    print("prime");
elif(flag==0):
    print("Not a prime");


