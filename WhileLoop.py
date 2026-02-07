#While loop to print the sum 
    # of first n natural number
n=int(input("enter a number:"))
count=1
sum=0
while(count<=n):
    sum=sum+count
    count=count+1
    
print("the sum of first",n,"natural number is:",sum)
