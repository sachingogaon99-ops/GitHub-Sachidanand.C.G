#Factorial of a given number
fact=1
n=int(input("enter a numbe:"))
if (n==0 or n==1):
    print("factorial of ",n,"is:",fact)
else:
    for i in range(1,n+1):
        fact=fact*i

        print("factorial of",n,"is:",fact)
